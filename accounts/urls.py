from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as authViews

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),

    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/delete/', views.delete_account, name='delete_account'),

    path(
        'reset_password/',
        authViews.PasswordResetView.as_view(
            template_name="accounts/password_reset.html",
            success_url=reverse_lazy('accounts:password_reset_done')
        ),
        name="reset_password"
    ),

    path(
        'reset_password_sent/',
        authViews.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_sent.html"
        ),
        name="password_reset_done"
    ),

    path(
        'reset/<uidb64>/<token>/',
        authViews.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_form.html",
            success_url=reverse_lazy('accounts:password_reset_complete')
        ),
        name="password_reset_confirm"
    ),

    path(
        'reset_password_complete/',
        authViews.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_complete"
    ),
]