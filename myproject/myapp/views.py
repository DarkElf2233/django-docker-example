from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.models import Book
from myapp.serializers import BookSerializer


class BookList(APIView):
    """
    List all books or create a new book.
    """

    def get(self, request):
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return Response(book_serializer.data)  

    def post(self, request):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
