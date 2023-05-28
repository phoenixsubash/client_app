from django.urls import path
from .views import *

urlpatterns = [
    path("login", create_client, name="login")
]
