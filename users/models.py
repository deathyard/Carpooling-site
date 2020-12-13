from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model): # A table of Profile in the database which is linked with the user model 
    user = models.OneToOneField(User,on_delete=models.CASCADE) # Every user will have 1 profile 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self): # Display the username when asked for profile object
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs): # save logic overwritten so that the uploaded picture gets resized to  smaller dimensions
        super().save(*args, **kwargs)

        img=Image.open(self.image.path)

        if img.height > 400 or img.width > 400:
            output_size = (400,400)
            img.thumbnail(output_size)
            img.save(self.image.path)


