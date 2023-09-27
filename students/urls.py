from django.urls import path
from . import views

urlpatterns = [
    path('generate-student/', views.generate_student, name='generate_student'),
    path('generate-students/', views.generate_students, name='generate_students'),
]