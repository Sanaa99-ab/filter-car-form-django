# polls/urls.py

# polls/urls.py

from django.urls import path
from . import views


urlpatterns = [
    # URL pattern for the car search form
    path('polls/search/', views.car_search_view, name='car_search'),
    # Other URL patterns for your app
    path('car-list/', views.car_list_view, name='car_list'),
]
