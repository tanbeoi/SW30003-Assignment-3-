from django.urls import path
from . import views

urlpatterns = [
    path('product_management/', views.product_view, name='product_management'),
]