from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addreq', views.addreq, name='addreq'),
    path('add_time', views.add_time, name='add_time')
]