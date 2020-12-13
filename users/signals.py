from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# To make the profile of the user automatically when a user registers

@receiver(post_save,sender = User) # receiving signal logic 
def create_profile(sender,instance,created,**kwargs): # creates the profile of the user
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender = User) # saving the profile of the user to the database
def save_profile(sender,instance,**kwargs):
        instance.profile.save()