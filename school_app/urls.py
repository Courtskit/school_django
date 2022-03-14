from django.urls import path
from . import views

urlpatterns = [
    path("students/all", views.list_students, name='list_students'),
]
