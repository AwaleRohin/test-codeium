from django.urls import path
from .views import add_client, client_list

urlpatterns = [
    path("add_client/", add_client, name="add_client"),
    path("", client_list, name="client_list"),
]
