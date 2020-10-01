
from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld),
    path('cookie', views.cookie),
  
]