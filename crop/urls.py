from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name = "store" ),
    path('upload_crop/',views.upload_crop,name = "upload_crop"),
    path('view_crops/',views.view_crops,name  = "view_crops"),
    path('store/',views.store , name  = "store"),
]
