from django.urls import path

from . import views

urlpatterns = [
    path('barang/', views.barang_list, name='barang-list'),
    path('barang/<int:pk>/', views.barang_detail, name='barang-detail'),
]
