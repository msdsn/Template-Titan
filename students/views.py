from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

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


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'title': 'Student List',
        'description': 'Welcome to the student list page!',
        'pageNum': '2',
    }
    return render(request, 'students/student_list.html', context)
    # return HttpResponse('Hello, world!')