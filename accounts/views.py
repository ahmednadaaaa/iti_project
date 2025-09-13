from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateNewUser, CustomerForm
from .models import Customer
from crowdfunding.models import Project, Donation
from .decorators import notLoggedUsers


@notLoggedUsers
def register(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{username} Created and Logged in Successfully!')
                return redirect('accounts:profile') 
    return render(request, 'accounts/register.html', {'form': form})


@notLoggedUsers
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username') or request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
        else:
            messages.info(request, 'Credentials error')
    return render(request, 'accounts/login.html')


@login_required
def userLogout(request):
    logout(request)
    return redirect('accounts:login')


@login_required
def profile_view(request):
    customer, created = Customer.objects.get_or_create(
        user=request.user,
        defaults={'name': request.user.username, 'email': request.user.email}
    )
    projects = Project.objects.filter(creator=request.user)
    donations = Donation.objects.filter(user=request.user)
    return render(
        request,
        'accounts/profile.html',
        {'customer': customer, 'projects': projects, 'donations': donations}
    )


@login_required
def edit_profile(request):
    customer, _ = Customer.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('accounts:profile')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def delete_account(request):
    customer, _ = Customer.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        password = request.POST.get('password')
        if request.user.check_password(password):
            # anonymize donations, delete projects handled by cascade
            Donation.objects.filter(user=request.user).update(user=None)
            request.user.delete()
            messages.success(request, 'Account deleted')
            return redirect('crowdfunding:home')
        else:
            messages.error(request, 'Incorrect password')
    return render(request, 'accounts/delete_account.html')