from django import forms
from .models import Project, Comment, Donation, Rating, ProjectReport, CommentReport
from .models import Donation, Payment, CashPayment
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'category', 'total_target', 'start_time', 'end_time', 'tags']

class ImageForm(forms.Form):
    images = forms.FileField(
        widget=MultiFileInput(attrs={'multiple': True}),
        required=False
    )
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']

class ProjectReportForm(forms.ModelForm):
    class Meta:
        model = ProjectReport
        fields = ['reason']

class CommentReportForm(forms.ModelForm):
    class Meta:
        model = CommentReport
        fields = ['reason']




class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'placeholder': 'Enter donation amount in EGP'
            })
        }
    
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Donation amount must be greater than zero.")
        return amount

class PaymentForm(forms.ModelForm):
    card_number = CardNumberField(label='Card Number')
    expire = CardExpiryField(label='Expiration Date')
    security_code = SecurityCodeField(label='CVV/CVC')
    
    class Meta:
        model = Payment
        fields = ['payment_method', 'shipment_address', 'shipment_phone', 'card_number', 'expire', 'security_code']
        widgets = {
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'shipment_address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Enter your address'}),
            'shipment_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
        }

class CashPaymentForm(forms.ModelForm):
    class Meta:
        model = CashPayment
        fields = ['shipment_address', 'shipment_phone']
        widgets = {
            'shipment_address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Enter your address'}),
            'shipment_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
        }