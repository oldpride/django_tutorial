from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# this is to automatically create profile everytime a user is created -tian
#   signal sender: User
#   signal receiver: below decorated functions
#   signal: 'post_save'
# this file needs to be imported by users/apps.py

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
