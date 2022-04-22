from django.shortcuts import render
import requests

# Create your views here.

def list(request):
    response = requests.get('http://127.0.0.1:8000/tasklist/')
    return render(request, 'frontend/list.html')
