from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Lesson

def lesson_page(request, id):
    lesson = get_object_or_404(Lesson, id=id)

    return render(request, "lessons/lesson_page.html", {
        "lesson": lesson
    })