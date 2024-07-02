import random

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    quotes = [
        "“You may delay, but time will not.” – Benjamin Franklin",
        "“Don’t wait. The time will never be just right.” – Napoleon Hill",
        "“Time is what we want most, but what we use worst.” – William Penn",
        # Add more quotes as needed
    ]
    quote = random.choice(quotes)
    return render(request, "home.html", {"quote": quote})
