from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='profes'),
    path('addreq', views.addreq, name='addreq'),
    path('replies', views.replies, name='replies'),
    path('add_time', views.add_time, name='add_time')
]