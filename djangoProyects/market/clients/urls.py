from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("",views.hello,name="hello"),
    path("",views.listClients,name="List"),
]