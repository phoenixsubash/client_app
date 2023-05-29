from django.urls import path
from .views import *

urlpatterns = [
    path("", create_client, name="create_client")
]
