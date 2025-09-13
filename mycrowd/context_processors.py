from django.conf import settings
def stripe_public_key(request):
    return {'STRIPE_PUBLIC_KEY': getattr(settings, 'STRIPE_PUBLIC_KEY', '')}
def recaptcha_site_key(request):
    return {'RECAPTCHA_SITE_KEY': getattr(settings, 'GOOGLE_RECAPTCHA_SITE_KEY', '')}
