from django.contrib import admin
from .models import SearchLog

@admin.register(SearchLog)
class SearchLogAdmin(admin.ModelAdmin):
    list_display = (
        "message",
        "user_ip",
        "city",
        "country",
        "device",
        "browser",
        "created_at"
    )

    search_fields = ("message", "user_ip", "city", "country")

    list_filter = ("country", "device", "browser", "created_at")