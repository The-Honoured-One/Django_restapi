from .models import Book, User
from django.http import JsonResponse
from .serializers import Myserializer, User_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status

@api_view(["GET", "POST"])
def func_books_with_id(request, id, format = None):
    if request.method == "GET":
        try:
            book_with_id = Book.objects.get(pk = id)
        except Book.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = Myserializer(book_with_id)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = Myserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(["GET"])
def func_books_without_id(request, format = None):
    books = Book.objects.all()
    serializer = Myserializer(books, many = True)
    return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
def func_users_with_id(request, id, format = None):
    try:
        users_with_id = User.objects.get(pk = id)
    except User.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = User_serializer(users_with_id)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = User_serializer(users_with_id, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        users_with_id.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def func_users_without_id(request, format = None):
    if request.method == "GET":
        users = User.objects.all()
        serializer = User_serializer(users, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = User_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED) 
