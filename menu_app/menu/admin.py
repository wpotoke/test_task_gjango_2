from django.contrib import admin
from menu.models import MainMenu, SubMenu

# Register your models here.
@admin.register(MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name", )}