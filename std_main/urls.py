from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendrep', views.send_reply, name='send_reply'),
]