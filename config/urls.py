from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('account.urls')),
    path('', include('trips.urls')),
    path('admin/', admin.site.urls),
]
