from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.BusinessList.as_view(), name='business_list'),
    path('<uuid:pk>/', views.BusinessDetail.as_view(), name='business_detail'),
    path('staffs/<uuid:pk>/', views.BusinessStaffDetail.as_view(), name='business_staff_detail'),
    path('services/', include('lessinline.api.business.services.urls')),
    path('bookings/', include('lessinline.api.business.bookings.urls')),
]
