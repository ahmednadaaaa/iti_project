from django.urls import path
from . import views
from .api import *
app_name = 'crowdfunding'

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/create/', views.create_project, name='create_project'),
    path('project/<int:pk>/donate/', views.donate_project, name='donate_project'),
    path('project/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('project/<int:pk>/rate/', views.rate_project, name='rate_project'),
    path('project/<int:pk>/cancel/', views.cancel_project, name='cancel_project'),
    path('project/<int:pk>/report/', views.report_project, name='report_project'),
    path('comment/<int:pk>/report/', views.report_comment, name='report_comment'),
    path('search/', views.project_search, name='project_search'),  
    path('project/<int:project_id>/donate/', views.create_donation, name='create_donation'),
    path('donation/<int:donation_id>/payment/', views.donation_payment, name='donation_payment'),
    path('donation/<int:donation_id>/card-payment/', views.card_payment, name='card_payment'),

    path('project/<int:project_id>/donate/', views.create_donation, name='create_donation'),

    

    path('api/categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('api/categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    
    path('api/tags/', TagListCreateView.as_view(), name='tag-list'),
    path('api/tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    
    path('api/projects/', ProjectListCreateView.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    
    path('api/project-images/', ProjectImageListCreateView.as_view(), name='projectimage-list'),
    path('api/project-images/<int:pk>/', ProjectImageDetailView.as_view(), name='projectimage-detail'),
    
    path('api/donations/', DonationListCreateView.as_view(), name='donation-list'),
    path('api/donations/<int:pk>/', DonationDetailView.as_view(), name='donation-detail'),
    
    path('api/ratings/', RatingListCreateView.as_view(), name='rating-list'),
    path('api/ratings/<int:pk>/', RatingDetailView.as_view(), name='rating-detail'),
    
    path('api/comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('api/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    
    path('api/project-reports/', ProjectReportListCreateView.as_view(), name='projectreport-list'),
    path('api/project-reports/<int:pk>/', ProjectReportDetailView.as_view(), name='projectreport-detail'),
    
    path('api/comment-reports/', CommentReportListCreateView.as_view(), name='commentreport-list'),
    path('api/comment-reports/<int:pk>/', CommentReportDetailView.as_view(), name='commentreport-detail'),
    
    path('api/payments/', PaymentListCreateView.as_view(), name='payment-list'),
    path('api/payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    
    path('api/cash-payments/', CashPaymentListCreateView.as_view(), name='cashpayment-list'),
    path('api/cash-payments/<int:pk>/', CashPaymentDetailView.as_view(), name='cashpayment-detail'),
    




]