from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookingList.as_view(), name='booking_list'),
    path('<uuid:pk>/', views.BookingDetail.as_view(), name='booking_detail')
]
