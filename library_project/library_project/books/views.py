from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class CreateBook(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get a list of all books
class ListBooks(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

# Update a book by ID
class UpdateBook(APIView):
    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a book by ID
class DeleteBook(APIView):
    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)