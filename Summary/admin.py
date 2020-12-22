from django.contrib import admin
from Summary.models import SummaryTable


@admin.register(SummaryTable)
class RiderAdmin(admin.ModelAdmin):
    list_display = ('name', 'matches', 'wins', 'draws', 'losers', 'bonus',
                    'small_points', 'year')
    search_fields = ('name', 'matches', 'wins', 'draws', 'losers', 'bonus',
                     'small_points', 'year')
    ordering = ('year', 'name')
