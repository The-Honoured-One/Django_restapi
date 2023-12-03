from rest_framework import serializers
from .models import Book, User

class Myserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author']

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']