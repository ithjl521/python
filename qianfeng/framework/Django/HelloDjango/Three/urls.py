from django.urls import path

from Three import views

urlpatterns = [
    path('three_index/', views.index),
]