from rest_framework import serializers
from .models import (
    Category, Tag, Project, ProjectImage, Donation, 
    Rating, Comment, ProjectReport, CommentReport,
    Payment, CashPayment
)
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)
    total_donated = serializers.SerializerMethodField()
    donation_percentage = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    days_left = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def get_total_donated(self, obj):
        try:
            return obj.total_donated()
        except:
            return 0
    
    def get_donation_percentage(self, obj):
        try:
            return obj.donation_percentage()
        except:
            return 0
    
    def get_average_rating(self, obj):
        try:
            return obj.average_rating()
        except:
            return 0
    
    def get_days_left(self, obj):
        try:
            # طريقة آمنة لحساب الأيام المتبقية
            from django.utils import timezone
            if hasattr(obj, 'end_time') and obj.end_time:
                if obj.end_time > timezone.now():
                    return (obj.end_time - timezone.now()).days
            return 0
        except:
            return 0

class DonationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    
    class Meta:
        model = Donation
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    
    class Meta:
        model = Rating
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'

class ProjectReportSerializer(serializers.ModelSerializer):
    reporter = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    
    class Meta:
        model = ProjectReport
        fields = '__all__'

class CommentReportSerializer(serializers.ModelSerializer):
    reporter = UserSerializer(read_only=True)
    comment = CommentSerializer(read_only=True)
    
    class Meta:
        model = CommentReport
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    donation = DonationSerializer(read_only=True)
    
    class Meta:
        model = Payment
        fields = '__all__'

class CashPaymentSerializer(serializers.ModelSerializer):
    donation = DonationSerializer(read_only=True)
    
    class Meta:
        model = CashPayment
        fields = '__all__'