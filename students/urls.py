from django.urls import path
from .views import home, student_list, student_add, student_edit, student_detail, student_delete

urlpatterns = [
    path('', home),
    path('students/', student_list, name='student-list'),
    path('students/add/', student_add),
    path('students/edit/<int:id>/', student_edit),
    path('students/detail/<int:id>/', student_detail),
    path('students/delete/<int:id>/', student_delete),
]