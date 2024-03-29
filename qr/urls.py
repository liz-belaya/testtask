from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.qr_list, name='qr_list'),
    path('qr/<int:pk>/', views.qr_detail, name='qr_detail'),
    path('qr/new/', views.qr_new, name='qr_new'),
    path('qr/<int:pk>/edit/', views.qr_edit, name='qr_edit'),
    path('qr/<pk>/remove/', views.qr_remove, name='qr_remove'),
    path('qr/<pk>/create/', views.qr_create, name='qr_create'),
    path('qr/<int:pk>/transition/', views.qr_transition, name='qr_transition'),
]


#if settings.DEBUG: # new
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
