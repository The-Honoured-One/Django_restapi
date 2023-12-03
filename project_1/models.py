from django.db import models

class Book(models.Model):
    name = models.CharField(max_length = 30)
    author = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.name} written by {self.author}"

class User(models.Model):
    name = models.CharField(max_length = 50)