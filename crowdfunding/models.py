from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True, null=True)
    def __str__(self): return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self): return self.name

class Project(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='projects')
    total_target = models.PositiveBigIntegerField()
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()
    tags = models.ManyToManyField(Tag, blank=True)
    featured = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_donated(self):
        return self.donations.aggregate(total=models.Sum('amount'))['total'] or 0

    def donation_percentage(self):
        if self.total_target==0: return 0
        return round(self.total_donated()*100/self.total_target,2)

    def average_rating(self):
        return self.ratings.aggregate(avg=models.Avg('value'))['avg'] or 0

    def can_cancel(self):
        return self.total_donated() < (0.25 * self.total_target)
    
    def days_left(self):
        if self.end_time > timezone.now():
            return (self.end_time - timezone.now()).days
        return 0

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        img = img.resize((600, 400))  
        img.save(self.image.path)

class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='donations')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='donations')
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)  

    def __str__(self):
        return f"Donation #{self.id} - {self.amount} EGP for {self.project.title}"
    
    
    
class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    class Meta:
        unique_together = ('project','user')

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    reported = models.BooleanField(default=False)

class ProjectReport(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reports')
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CommentReport(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reports')
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
    ]
    
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    shipment_address = models.CharField(max_length=150, blank=True, null=True)
    shipment_phone = models.CharField(max_length=50, blank=True, null=True)
    card_number = CardNumberField(blank=True, null=True)
    expire = CardExpiryField(blank=True, null=True)
    security_code = SecurityCodeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.donation.is_paid = True
        self.donation.save()
    
    def __str__(self):
        return f"Payment for Donation #{self.donation.id}"

class CashPayment(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, related_name='cash_payments')
    shipment_address = models.CharField(max_length=150)
    shipment_phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False) 
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_confirmed:
            self.donation.is_paid = True
            self.donation.save()
    
    def __str__(self):
        return f"Cash Payment for Donation #{self.donation.id}"