from django.shortcuts import render

# chatapp/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'chatapp/index.html')
