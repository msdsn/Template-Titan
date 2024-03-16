from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'students/home.html', context)
    # return HttpResponse('Hello, world!')