from django.db.models.signals import post_save
from .models import Profile

def profileUpdate(sender, instance, created, **kwargs):
    print("Profile Updated!")

post_save.connect(profileUpdate, sender=Profile)