from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_vectors, name='calculate_vectors')
]