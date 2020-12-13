from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Trip
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#Dummy data which was used for testing purpose

# trips = [
#     {
#         'author':'Utk',
#         'source':'Mumbai',
#         'destination':'Hyderabad',
#         'vacant_seats':4,
#         'date_of_trip':'August 4,208'
#     },
#     {
#         'author':'sda',
#         'source':'Mum',
#         'destination':'Hyderd',
#         'vacant_seats':8,
#         'date_of_trip':'August 8,2018'
#     }
# ]


def home(request):   # Home Page Logic
    return render(request,'carpool/home.html')

class TripListView(ListView): # List of all trips logic
    model = Trip
    template_name = 'carpool/trips.html'
    context_object_name='trips'    
    ordering = ['date_of_trip']   # to display latest trip by date before
    paginate_by = 5                

class UserTripListView(ListView): # List of all trips of a specific user logic
    model = Trip
    template_name = 'carpool/user_trips.html'
    context_object_name='trips'
    

    def get_queryset(self):     # Return trips of a specific user 
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Trip.objects.filter(author=user).order_by('date_of_trip')

class TripDetailView(DetailView): # Detailed representation of a trip logic 
    model = Trip

class TripDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): # Deleteing a trip Logic
    model = Trip
    success_url = '/carpool/trip'

    def test_func(self): # Can be deleted only by the user who created it
        trip = self.get_object()
        if self.request.user == trip.author:
            return True
        return False


class TripCreateView(LoginRequiredMixin, CreateView): # Creating a trip Logic 
    model = Trip
    fields = ['source','destination','vacant_seats','date_of_trip']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TripUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView): # Updating a trip Logic
    model = Trip
    fields = ['source','destination','vacant_seats','date_of_trip']

    def form_valid(self,form):  # taking in the update information from the user                      
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # Can be updated by the user who created it 
        trip = self.get_object()
        if self.request.user == trip.author:
            return True
        return False

def contact(request):
    return render(request,'carpool/contactform.html')

def trip(request):  # Function based view of all trips(Currently not using, Using class based view instead)
    context={
        'trips':Trip.objects.all()
    }
    return render(request,'carpool/trips.html',context)

def navigate(request): # navigate page logic
    return render(request,'carpool/navigate.html')


def about(request): # about page logic
    return render(request,'carpool/about.html')