from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.health),
    path('api/auth/', include('lessinline.api.auth.urls')),
    path('api/business/', include('lessinline.api.business.urls')),
]
