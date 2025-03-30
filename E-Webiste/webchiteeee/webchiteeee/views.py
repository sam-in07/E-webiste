# Importing necessary modules from Django
from django.http import HttpResponse  # This is used for returning raw HTTP responses.
from django.shortcuts import render  # This is used for rendering templates.

# Define the view function for the 'home' page
def home(request):
    # Render the "home.html" template and return an HttpResponse with the rendered content
    # 'request' is passed automatically by Django to get information about the incoming request.
    # The template "home.html" will be processed and populated with any dynamic content (if any).
    return render(request, "home.html")
