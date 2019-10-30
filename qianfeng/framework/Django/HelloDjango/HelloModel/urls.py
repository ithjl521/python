from django.urls import path

from HelloModel import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('addperson/', views.addperson, name='addperson'),
    path('addidcard/', views.addidcard, name='addidcard'),
    path('bindcard/', views.bindcard, name='bindcard'),
    path('removeperson/', views.removeperson, name='removeperson'),
    path('removeidcard/', views.removeidcard, name='removeidcard'),
    path('getpersonbycard/', views.getpersonbycard, name='getpersonbycard'),
    path('getidcardbyperson/', views.getidcardbyperson, name='getidcardbyperson'),
]