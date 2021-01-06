from django.urls import path, register_converter
from Riders import views
from Summary import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('riders/', views.RiderListView.as_view(), name='riders'),
    path('ridersinfo/', views.RiderInfoView.as_view(), name='ridersinfo'),
    path('ridersinfo/<yyyy:year>/<team_id>',
         views.TeamRidersList.as_view(),
         name='ridersinfo'
         ),
    path('riders/<rider_id>', views.RiderView.as_view(), name='rider')
    ]
