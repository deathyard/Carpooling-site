from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Trip(models.Model): # To have a table of trip in the database along with the below attributes 
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    vacant_seats = models.IntegerField()
    date_of_trip = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Linking the user model and the trip model

    def __str__(self): # Display an object of trip as "source to destination"
        title = self.source + ' to ' + self.destination
        return title

    def get_absolute_url(self): # Returns URL for detailed view of a trip
        return reverse('trip-detail',kwargs={'pk':self.pk})