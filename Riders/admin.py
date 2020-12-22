from django.contrib import admin
from Riders.models import RiderInfo, Rider


@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birthday', 'nationality')
    search_fields = ('last_name', 'first_name', 'birthday', 'nationality')
    ordering = ('last_name',)


@admin.register(RiderInfo)
class RiderAdmin(admin.ModelAdmin):
    list_display = ('rider', 'team', 'year', 'junior')
    search_fields = ('rider', 'team', 'year', 'junior')
    ordering = ('rider',)
