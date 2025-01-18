from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_request_view, name='create_request'),
    path('track/', views.track_request_view, name='track_request'),
]
