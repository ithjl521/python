from django.urls import path

from App import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('template/', views.HelloTemplateView.as_view(), name='template'),
    path('listview/', views.HelloListView.as_view(), name='listview'),
    path('single/<int:pk>/', views.HelloDetailView.as_view(), name='single'),

]