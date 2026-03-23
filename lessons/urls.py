from django.urls import path
from .views import lesson_page

urlpatterns = [

    path('lesson/<int:id>/', lesson_page, name='lesson_page'),

]