from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'title': 'Home',
        'description': 'Welcome to the home page!',
        'pageNum': '1',
        'authorsList': [
            "Author1",
            "Author2",
            "Author3",
        ],
        'authorsDict': {
            "key1": 1,
            "key2": 2,
        }

    }
    return render(request, 'students/home.html', context)
    # return HttpResponse('Hello, world!')