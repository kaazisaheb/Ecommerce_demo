from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('like/<int:product_id>/', views.like_product, name='like_product'),
    
]
