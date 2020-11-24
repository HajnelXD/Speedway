from django.urls import path, register_converter

from Matches import views
from Summary import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path(
        'season_matches/<yyyy:year>',
        views.SeasonMatchesView.as_view(),
        name='season_matches'
    ),
    path(
        'match_points/<identifier>',
        views.MatchPointsView.as_view(),
        name='match_points'
    ),
]
