from django.urls import path
from Teams import views


urlpatterns = [
    path('years/', views.YearsList.as_view(), name='years'),
    path('teams/', views.TeamsList.as_view(), name='teams'),
]
