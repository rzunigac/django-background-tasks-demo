from django.urls import path
from . import views

urlpatterns = [
    path('', views.trigger_email, name='trigger_email'),
    path('success/', views.success, name='success'),
]
