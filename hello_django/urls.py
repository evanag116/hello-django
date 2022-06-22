"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from math import pi


def rectangle_area(request, height, width):
    area = HttpResponse(f"The area of a rectangle with dimensions {height}x{width} is {height * width}.")
    return area
    

def rectangle_perimeter(request, height, width):
    perimeter = HttpResponse(f"The perimeter of a rectangle with dimensions {height}x{width} is {(2 * height) + (2 * width)}.")
    return perimeter

def circle_area(request, radius):
    area = HttpResponse(f"The area of circle with radius {radius} is {round((pi * radius**2), 2)}.")
    return area

def circle_perimeter(request, radius):
    circumference = HttpResponse(f"The circumference of a circle with radius {radius} is {round((2 * radius * pi), 2)}.")
    return circumference



urlpatterns = [
    path('admin/', admin.site.urls), 
    path('rectangle/area/<int:height>/<int:width>', rectangle_area),
    path('rectangle/perimeter/<int:height>/<int:width>', rectangle_perimeter),
    path('circle/area/<int:radius>', circle_area),
    path('circle/perimeter/<int:radius>', circle_perimeter)
]