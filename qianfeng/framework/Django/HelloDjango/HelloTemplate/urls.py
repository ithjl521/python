from django.urls import path

from HelloTemplate import views

urlpatterns = [
    path('hello', views.hello),
    path('get_students', views.get_students),
    path('home/', views.home),
    path('home_mine/', views.home_mine),
]