from django.urls import path
from .views import *

urlpatterns = [
    path("create_client", create_client, name="create_client"),
    path("client_list", client_list, name="client_list"),
    path("", login_view, name="login")
]
