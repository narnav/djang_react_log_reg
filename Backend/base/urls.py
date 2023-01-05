from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # authenticate
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', views.register),
    path('', views.index),
    path('test', views.test),
    path('products', views.products),

]
