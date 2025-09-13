from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg, Q, Count
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Project, Category, ProjectImage, Donation, Rating, Comment
from .models import Project, Category, ProjectImage, Donation, Rating, Comment, ProjectReport, CommentReport
from .forms import ProjectForm, ImageForm, DonationForm, CommentForm, RatingForm, ProjectReportForm, CommentReportForm
from .filters import ProjectFilter  
from .models import Project, Donation, Payment, CashPayment
from .forms import DonationForm, PaymentForm, CashPaymentForm



def home(request):
    top_rated = Project.objects.filter(is_canceled=False, end_time__gt=timezone.now())\
    .annotate(avg=Avg('ratings__value'))\
    .order_by('-avg')[:5]

    latest_projects = Project.objects.filter(is_canceled=False).order_by('-created_at')[:5]
    featured_projects = Project.objects.filter(featured=True, is_canceled=False).order_by('-created_at')[:5]
    categories = Category.objects.all()

    project_list = Project.objects.filter(is_canceled=False)
    search_filter = ProjectFilter(request.GET, queryset=project_list)

    return render(request, 'home1.html', {
        'top_rated_projects': top_rated,
        'latest_projects': latest_projects,
        'featured_projects': featured_projects,
        'categories': categories,
        'search_filter': search_filter,
        'search_results': search_filter.qs,
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    images = project.images.all()
    comments = project.comments.filter(parent__isnull=True).order_by('-created_at')

    stats = project.ratings.aggregate(
        avg_rating=Avg('value'),
        reviews_count=Count('id')
    )
    avg_rating = stats['avg_rating'] or 0
    reviews_count = stats['reviews_count']

    similar = Project.objects.filter(tags__in=project.tags.all()).exclude(pk=pk).distinct()[:4]
    donation_form = DonationForm()
    comment_form = CommentForm()
    rating_form = RatingForm()

    return render(request, 'projects/project_detail.html', {
        'project': project,
        'images': images,
        'comments': comments,
        'avg_rating': avg_rating,
        'reviews_count': reviews_count,
        'similar': similar,
        'donation_form': donation_form,
        'comment_form': comment_form,
        'rating_form': rating_form
    })

def project_search(request):
    project_list = Project.objects.filter(is_canceled=False)
    
    search_filter = ProjectFilter(request.GET, queryset=project_list)
    search_results = search_filter.qs
    
    search_results = search_results.order_by('-created_at')
    
    paginator = Paginator(search_results, 9)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    return render(request, 'projects/project_search.html', {
        'search_filter': search_filter,
        'search_results': page_obj,
        'categories': categories,
        'now': timezone.now(),
    })

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        img_form = ImageForm(request.POST, request.FILES)
        if form.is_valid() and img_form.is_valid():
            project = form.save(commit=False)
            project.creator = request.user
            project.save()
            form.save_m2m()
            images = request.FILES.getlist('images')
            for img in images:
                ProjectImage.objects.create(project=project, image=img)
            messages.success(request,'Project created')
            return redirect('crowdfunding:project_detail', pk=project.pk)
    else:
        form = ProjectForm()
        img_form = ImageForm()
    return render(request,'projects/create_project.html', {'form':form, 'img_form':img_form})

@login_required
def donate_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.project = project
            donation.save()
            messages.success(request,'Thank you for your donation')
    return redirect('crowdfunding:project_detail', pk=pk)

@login_required
def add_comment(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        parent_id = request.POST.get('parent')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.project = project
            if parent_id:
                try:
                    comment.parent = Comment.objects.get(pk=parent_id)
                except Comment.DoesNotExist:
                    comment.parent = None
            comment.save()
            messages.success(request,'Comment added')
    return redirect('crowdfunding:project_detail', pk=pk)

@login_required
def report_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.project = project
            report.save()
            messages.success(request,'Project reported')
    return redirect('crowdfunding:project_detail', pk=pk)

@login_required
def report_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.comment = comment
            report.save()
            messages.success(request, 'Comment reported successfully')
    return redirect('crowdfunding:project_detail', pk=comment.project.pk)

@login_required
def rate_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            rating, created = Rating.objects.update_or_create(project=project, user=request.user, defaults={'value':value})
            messages.success(request,'Rating saved')
    return redirect('crowdfunding:project_detail', pk=pk)

@login_required
def cancel_project(request, pk):
    project = get_object_or_404(Project, pk=pk, creator=request.user)
    if project.can_cancel():
        project.is_canceled = True
        project.save()
        messages.success(request,'Project cancelled')
    else:
        messages.error(request,'Cannot cancel. Donations >= 25%')
    return redirect('crowdfunding:project_detail', pk=pk)



def create_donation(request, project_id):
    if not request.user.is_authenticated:
        messages.info(request, 'Please log in to make a donation.')
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.project = project
            donation.save()
            
            messages.success(request, 'Thank you for your donation!')
            return redirect('crowdfunding:project_detail', pk=project.id)
    else:
        form = DonationForm()
    
    return render(request, 'create_donation.html', {
        'form': form,
        'project': project
    })
@login_required
def donation_payment(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id, user=request.user)
    
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        if payment_method == 'card':
            return redirect('crowdfunding:card_payment', donation_id=donation.id)
        elif payment_method == 'cash':
            return redirect('crowdfunding:cash_payment', donation_id=donation.id)
    
    return render(request, 'donations/payment_method.html', {
        'donation': donation
    })

@login_required
def card_payment(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id, user=request.user)
    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.donation = donation
            payment.save()
            
            messages.success(request,'done !')
            return redirect('crowdfunding:project_detail', pk=donation.project.pk)
    else:
        form = PaymentForm()
    
    return render(request, 'donations/card_payment.html', {
        'form': form,
        'donation': donation
    })

@login_required
def cash_payment(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id, user=request.user)
    
    if request.method == 'POST':
        form = CashPaymentForm(request.POST)
        if form.is_valid():
            cash_payment = form.save(commit=False)
            cash_payment.donation = donation
            cash_payment.save()
            
            messages.success(request, 'done')
            return redirect('crowdfunding:project_detail', pk=donation.project.pk)
    else:
        form = CashPaymentForm()
    
    return render(request, 'donations/cash_payment.html', {
        'form': form,
        'donation': donation
    })