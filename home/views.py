from django.shortcuts import render

def index(request):  # контроллер
    return render(request, 'home/home.html')
