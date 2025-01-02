
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.ListBooks.as_view(), name='book_list'),  
    path('books/create/', views.CreateBook.as_view(), name='create_book'),  
    path('books/update/<int:pk>/', views.UpdateBook.as_view(), name='update_book'), 
    path('books/delete/<int:pk>/', views.DeleteBook.as_view(), name='delete_book'),  
]
