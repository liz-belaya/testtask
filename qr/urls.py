from django.urls import path
from . import views

urlpatterns = [
    path('', views.qr_list, name='qr_list'),
    path('qr/<int:pk>/', views.qr_detail, name='qr_detail'),
    path('qr/new/', views.qr_new, name='qr_new'),
    path('qr/<int:pk>/edit/', views.qr_edit, name='qr_edit'),
]
