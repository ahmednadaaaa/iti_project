from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Category, Tag, Project, ProjectImage, Donation, 
    Rating, Comment, ProjectReport, CommentReport,
    Payment, CashPayment
)
from .serializers import (
    CategorySerializer, TagSerializer, ProjectSerializer,
    ProjectImageSerializer, DonationSerializer, RatingSerializer,
    CommentSerializer, ProjectReportSerializer, CommentReportSerializer,
    PaymentSerializer, CashPaymentSerializer
)

# Category API Views
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Tag API Views
class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Project API Views
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'tags', 'featured', 'is_canceled']
    search_fields = ['title', 'details']
    ordering_fields = ['created_at', 'total_target', 'start_time', 'end_time']

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# ProjectImage API Views
class ProjectImageListCreateView(generics.ListCreateAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProjectImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Donation API Views
class DonationListCreateView(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['project', 'user']
    ordering_fields = ['created_at', 'amount']

class DonationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Rating API Views
class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project', 'user']

class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Comment API Views
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['project', 'user', 'reported']
    ordering_fields = ['created_at']

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# ProjectReport API Views
class ProjectReportListCreateView(generics.ListCreateAPIView):
    queryset = ProjectReport.objects.all()
    serializer_class = ProjectReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['project', 'reporter']
    ordering_fields = ['created_at']

class ProjectReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectReport.objects.all()
    serializer_class = ProjectReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# CommentReport API Views
class CommentReportListCreateView(generics.ListCreateAPIView):
    queryset = CommentReport.objects.all()
    serializer_class = CommentReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['comment', 'reporter']
    ordering_fields = ['created_at']

class CommentReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentReport.objects.all()
    serializer_class = CommentReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Payment API Views
class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['donation']
    ordering_fields = ['created_at']

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# CashPayment API Views
class CashPaymentListCreateView(generics.ListCreateAPIView):
    queryset = CashPayment.objects.all()
    serializer_class = CashPaymentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['donation']
    ordering_fields = ['created_at']

class CashPaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CashPayment.objects.all()
    serializer_class = CashPaymentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]