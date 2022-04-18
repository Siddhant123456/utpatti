from django.urls import path
from . import views


urlpatterns = [
    path('place-bid' , views.place_bid , name = "place_bid"),
    path('create-bid/<int:id>', views.create_bid , name = "create_bid"),
]
