# Importing the 'path' function from Django to define URL patterns
from django.urls import path

# Importing views from the current package to map URLs to view functions
from . import views

# Defining the URL patterns list for the app
urlpatterns = [
    # Mapping the root URL ('') to the 'home' view, with the name 'home' for reference
    path('', views.home, name='home'),

    # Mapping the 'add/' URL to the 'add_expense' view, with the name 'add_expense' for reference
    path('add/', views.add_expense, name='add_expense'),
]
