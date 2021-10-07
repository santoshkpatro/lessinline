from django.urls import path, include

urlpatterns = [
    path('businesses/', include('lessinline.api.public.businesses.urls')),
    path('services/', include('lessinline.api.public.services.urls')),
    path('bookings/', include('lessinline.api.public.bookings.urls')),
]
