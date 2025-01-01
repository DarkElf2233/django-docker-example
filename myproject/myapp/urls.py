from django.urls import path
from myapp import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
]
