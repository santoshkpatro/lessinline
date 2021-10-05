from django.urls import path
from . import views


urlpatterns = [
    path('<uuid:pk>/', views.ServiceDetail.as_view(), name='service_detail')
]
