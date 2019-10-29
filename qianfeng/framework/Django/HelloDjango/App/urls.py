from django.conf.urls import url
from django.urls import path

from App import views

urlpatterns = [
    path('other_urls/', views.other_urls),
    path('add_student/', views.add_student),
    path('get_students/', views.get_students),
    path('update_student/', views.update_student),
    path('delete_student/', views.delete_student),
    path('add_person/', views.add_person),
    path('add_persons/', views.add_persons),
    path('get_persons/', views.get_persons),
    path('get_person/', views.get_person),
]
