# accounts/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer

@receiver(post_save, sender=User)
def create_or_update_customer(sender, instance, created, **kwargs):
    print("SIGNAL: post_save User fired. created:", created, "username:", getattr(instance, 'username', None))
    if created:
        Customer.objects.get_or_create(
            user=instance,
            defaults={
                'name': instance.username or '',
                'email': instance.email or ''
            }
        )
    else:
        try:
            cust, _ = Customer.objects.get_or_create(user=instance)
            updated = False
            if instance.username and cust.name != instance.username:
                cust.name = instance.username; updated = True
            if instance.email and cust.email != instance.email:
                cust.email = instance.email; updated = True
            if updated:
                cust.save()
        except Exception as e:
            print("SIGNAL ERROR updating Customer:", e)