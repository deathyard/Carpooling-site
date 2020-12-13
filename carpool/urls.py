from django.urls import path
from . import views 
from .views import TripListView,TripDetailView,TripCreateView,TripUpdateView,TripDeleteView,UserTripListView

# All the routes associated with the carpool webapp
urlpatterns = [
    path('', views.home,name='carpool-home'),
    path('trip/<int:pk>/', TripDetailView.as_view(),name='trip-detail'),
    path('trip/<int:pk>/update', TripUpdateView.as_view(),name='trip-update'),
    path('trip/<int:pk>/delete', TripDeleteView.as_view(),name='trip-delete'),
    path('trip/new/', TripCreateView.as_view(),name='trip-create'),
    path('trip', TripListView.as_view(),name='carpool-trip'),
    path('trip/user/<str:username>', UserTripListView.as_view(),name='user-trips'),
    path('about/', views.about,name='carpool-about'),
    path('navigate/', views.navigate,name='carpool-navigate'),
    path('contact/', views.contact,name='carpool-contact'),

]
