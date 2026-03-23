from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from lessons.models import Lesson
from .models import Course

def home(request):
    courses = Course.objects.all()[:6]
    return render(request, "home.html", {"courses": courses})

def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})


def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    lessons = Lesson.objects.filter(course=course)

    context = {
        "course": course,
        "lessons": lessons
    }

    return render(request, "courses/course_detail.html", context)