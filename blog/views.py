from django.http import HttpResponse

# Define a view for the home page
def home_view(request):
    return HttpResponse('<h1>Welcome to My Blog</h1>')