from django.contrib import admin
from django.urls import path
from blog.views import home_view  # Import the home view from the blog app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Route for the home page
]