from django.urls import path, include
from . import views


app_name = 'TRP'

urlpatterns = [
    path('', views.home, name='home'),
    path('start/date', views.start_date, name='start_date'),
    path('calculate/', views.calculate, name='calculate'),
]