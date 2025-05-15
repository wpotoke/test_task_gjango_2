from django.contrib import admin
from menu.models import MenuItem

# Register your models here.
@admin.register(MenuItem)
class MainMenuAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "parent", "menu_name"]
    