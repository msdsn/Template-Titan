from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

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

def student_add(request):
    form = StudentForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        print('Printing FILES:', request.FILES)
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    context = {
        'form': form,
    }
    return render(request, 'students/student_add.html', context)
    # return HttpResponse('Hello, world!')


def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    context = {
        'form': form,
    }
    return render(request, 'students/student_edit.html', context)
    # return HttpResponse('Hello, world!')

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student,
    }
    return render(request, 'students/student_detail.html', context)
    # return HttpResponse('Hello, world!')

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student-list')
    context = {
        'student': student,
    }
    return render(request, 'students/student_delete.html', context)
    # return HttpResponse('Hello, world!')