from django.contrib import admin
from menu.models import MainMenu

# Register your models here.
@admin.register(MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    list_display = ["name"]
