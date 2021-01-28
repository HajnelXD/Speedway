from django.contrib import admin
from Riders.models import RiderInfo, Rider


@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birthday', 'nationality')
    search_fields = ('last_name', 'first_name', 'birthday', 'nationality')
    ordering = ('last_name',)


@admin.register(RiderInfo)
class RiderInfoAdmin(admin.ModelAdmin):
    list_display = ('rider', 'team', 'year', 'junior')
    search_fields = (
        'rider__last_name',
        'rider__first_name',
        'team__team_name',
        'year__year',
        'junior'
    )
    ordering = ('rider',)
