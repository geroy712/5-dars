from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Course, Student


def home(request: WSGIRequest):
    courses = Course.objects.all()
    students = Student.objects.all()
    context = {
        "courses": courses,
        "students": students
    }
    return render(request, "intex.html", context)

def course(request, course_id):
    courses = Course.objects.all()
    students = Student.objects.filter(course_id=course_id)

    context = {
        "courses": courses,
        "students": students
    }
    return render(request, 'index.html', context)