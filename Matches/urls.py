from django.urls import path, register_converter

from Matches import views
from Summary import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path(
        'season_matches/<yyyy:year>',
        views.SeasonMatchesView.as_view(),
        name='season_matches',
    ),
    path(
        'match_points/<identifier>',
        views.MatchPointsView.as_view(),
        name='match_points',
    ),
    path(
        'team_riders_points/<team_id>/<yyyy:year>',
        views.TeamRidersPoints.as_view(),
        name='team_riders_points',
    ),
    path(
        'rider_stas_vs/<home_team_id>/<team_id>/<yyyy:year>',
        views.RiderStatsVs.as_view(),
        name='rider_stats_vs',
    ),
    path(
        'match_points/<rider_id>',
        views.RiderMatchPoints,
        name='rider match points'
    )
]
