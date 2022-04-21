from django.shortcuts import render

# Create your views here.

def list(request):
    response = request.get('http://127.0.0.1:8000/tasklist/')
    print(response)
    return render(request, 'frontend/list.html')
