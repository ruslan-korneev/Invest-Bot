from django.contrib import admin
from apps.invest_admin_app.models import Crypto, Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "date_created")
    list_filter = ("country", "date_created")


@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    list_display = ("name", "date_created")
    list_filter = ("date_created",)
