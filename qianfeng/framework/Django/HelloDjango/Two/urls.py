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
    path('hello_response/', views.hello_response, name='response'),
    path('getticket/', views.getticket, name='getticket'),  # 重定向
    path('get_info/', views.get_info, name='get_info'),  # JsonResponse

    # cookie
    path('set_cookie/', views.set_cookie, name='set_cookie'),
    path('get_cookie/', views.get_cookie, name='get_cookie'),

    # session
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),

    # token
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('mine/', views.mine, name='mine'),
]
