from django.urls import path

from App import views

urlpatterns = [
    path('home/', views.home, name='home'),

    path('market/', views.market, name='market'),

    path('cart/', views.cart, name='cart'),

    path('mine/', views.mine, name='mine'),
    path('market_with_params/<int:typeid>/<int:childcid>/<int:order_rule>/', views.market_with_params, name='market_with_params'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('checkuser/', views.check_user, name='check_user'),

    path('logout/', views.logout, name='logout'),

    path('activate/', views.activate, name='activate'),

    path('addtocart/', views.add_to_cart, name='add_to_cart'),
    path('changecartstate/', views.change_cart_state, name='change_cart_state'),
    path('subshopping/', views.sub_shopping, name='sub_shopping'),
    path('allselect/', views.all_select, name='all_select'),

    path('makeorder/', views.make_order, name='make_order'),

]
