from django.contrib import admin
from .models import SayLog


@admin.register(SayLog)
class SayLogAdmin(admin.ModelAdmin):
    list_display = ("message",)
    search_fields = ("message",)
