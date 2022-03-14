from tkinter import Entry
from django.shortcuts import render
from .models import Student 


def list_students(request):
    my_data = {
        "all_students": Student.objects.all() # SELECT * FROM school_app_student
    }
    return render(request, "pages/list_students.html", my_data)
