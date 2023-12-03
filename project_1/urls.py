"""
URL configuration for project_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project_1 import views
from rest_framework.urlpatterns import format_suffix_patterns 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.func_books_without_id),
    path('books/<int:id>', views.func_books_with_id),
    path('users/<int:id>', views.func_users_with_id),
    path('users/', views.func_users_without_id)
]

urlpatterns = format_suffix_patterns(urlpatterns)
