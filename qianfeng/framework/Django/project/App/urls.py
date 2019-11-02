from django.urls import path

from App import views

urlpatterns = [
    path('home/', views.home, name='home'),

    path('market/', views.market, name='market'),

    path('cart/', views.cart, name='cart'),

    path('mine/', views.mine, name='mine'),
]