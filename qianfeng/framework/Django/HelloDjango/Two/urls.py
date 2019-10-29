from django.conf.urls import url
from django.urls import path

from Two import views

urlpatterns = [
    # url('students/$', views.students),
    # url('students/(\d+)/', views.student),
    path('students/', views.students),
    path('students/<str:s_id>/', views.student),
    path('get_time/<str:h>/<str:m>/<str:s>', views.get_time, name='get_time'),

    path('learn/', views.learn, name='learn'),

    path('have_request/', views.have_request),
]
