from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Frontend view
    path("chat/", views.chat_view, name="chat_view"),  # API for chat
    path("terms/", views.ter, name="Terms"),  # API for chat
]
