from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServiceList.as_view(), name='service_list'),
    path('<uuid:pk>/', views.ServiceDetail.as_view(), name='service_detail')
]
