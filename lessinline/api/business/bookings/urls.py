from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookingsList.as_view(), name='bookings_list'),
    path('<uuid:pk>/', views.BookingDetail.as_view(), name='bookings_list')
]
