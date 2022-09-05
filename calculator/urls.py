from django.contrib import admin
from django.urls import path, include
from TRP import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('TRP/', include('TRP.urls')),
    path('common/', include('common.urls')),
    path('', views.home)
]
