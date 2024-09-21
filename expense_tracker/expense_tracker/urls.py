"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importing the 'admin' module from Django to configure the admin interface
from django.contrib import admin

# Importing the 'path' and 'include' functions to define URL patterns and include other URL configurations
from django.urls import path, include

# Defining the root URL patterns for the project
urlpatterns = [
    # Mapping the 'admin/' URL to Django's default admin site
    path('admin/', admin.site.urls),

    # Including the URL patterns from the 'tracker' app. The empty string ('') means the tracker app's URLs will be accessible from the root
    path('tracker/', include('tracker.urls')),
]

