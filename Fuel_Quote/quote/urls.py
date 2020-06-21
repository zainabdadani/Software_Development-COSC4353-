from django.urls import path
from . import views

urlpatterns = [
    path('quote/', views.quote),
    path('history/', views.history),
    path('registerClient/', views.registerClient)
]