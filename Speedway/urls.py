from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/teams/', include('Teams.urls')),
    path('api/riders/', include('Riders.urls')),
    path('api/matches/', include('Matches.urls')),
]
