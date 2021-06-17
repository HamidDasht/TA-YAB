from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendrep', views.send_reply, name='send_reply'),
    path('bookmark_request', views.bookmark_request, name='bookmark_request'),
]