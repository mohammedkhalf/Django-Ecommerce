from django.urls import path,include
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/info', views.product_info),
    path('products/<int:pk>/', views.product_details),
    path('orders/', views.order_list),
    path('silk/', include('silk.urls', namespace='silk')),
]
