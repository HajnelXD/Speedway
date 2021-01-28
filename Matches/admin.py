from django.contrib import admin
from Matches.models import Match, MatchPoints


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'home_team',
        'home_team_points',
        'guest_team_points',
        'guest_team',
        'date',
        'isFinished',
        'queue',
    )
    search_fields = (
        'home_team__team_name',
        'guest_team__team_name',
        'date',
        'isFinished',
        'queue',
        'playoff',
    )
    ordering = ('date',)


@admin.register(MatchPoints)
class MatchPointsAdmin(admin.ModelAdmin):
    list_display = (
        'rider',
        'match',
        'runs',
        'bonuses',
        'team',
        'number',
        'joker_rider'
    )
    search_fields = (
        'rider__last_name',
        'match__home_team__team_name',
        'match__guest_team__team_name',
        'runs', 'bonuses', 'team__team_name',
        'number',
    )
    ordering = ('rider__last_name',)
