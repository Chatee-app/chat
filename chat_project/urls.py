from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('api/', include('chat.urls')),  # Include your app's URLs under /api/
    path('', include('chat.urls')),  # Include your app's URLs for root path
]
