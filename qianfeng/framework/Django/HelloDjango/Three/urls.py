from django.urls import path

from Three import views

urlpatterns = [
    path('three_index/', views.index),
    path('getuser/', views.get_user),
    path('getusers/', views.get_users),
    path('getorders/', views.get_orders),
    path('getgrades/', views.getgrades),
    path('getcustomer/', views.getcustomer),
    path('getcompany/', views.getcompany),
    path('getanimals/', views.getanimals),
]