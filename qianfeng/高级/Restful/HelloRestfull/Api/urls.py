from django.urls import path

from Api import views

urlpatterns = {

    path('books/', views.books, name='books'),
    path('books/<int:book_id>/', views.book, name='book'),

}