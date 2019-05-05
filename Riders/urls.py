from django.urls import path
from Riders import views


urlpatterns = [
    path('riders/', views.RiderListView.as_view(), name='riders'),
    ]
