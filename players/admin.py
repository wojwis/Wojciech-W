from django.contrib import admin
from .models import Players

@admin.register(Players)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'numer_startowy', 'nazwisko', 'imie',
                       'kat_wiekowa', 'oplacony', 'bieg', 'data_zapisu', 'nazwisko_rodzic',
                     'email_rodzic']
    search_fields = ['nazwisko']
    list_filter = ['kat_wiekowa','oplacony','bieg','miasto']




