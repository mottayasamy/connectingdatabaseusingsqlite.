from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('products/', views.read_products, name='read_products'),
    path('<int:pk>/update/', views.update_product, name='update_product'),
    path('<int:pk>/delete/', views.delete_product, name='delete_product'),
]
