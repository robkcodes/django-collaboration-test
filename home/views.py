from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    """
    Returns Hello Message
    """
    return render(request, "home/index.html")
