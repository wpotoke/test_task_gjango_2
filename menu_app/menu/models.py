from django.db import models

class MenuItem(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name="Имя пункта меню")
    url = models.CharField(max_length=100, unique=True, verbose_name="URL")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="items", verbose_name="Главное меню", null=True, blank=True)
    menu_name = models.CharField(max_length=100, verbose_name="Название меню")
    
    class Meta:
        db_table = "sub_menu"
        verbose_name = "Вложенное меню"
        verbose_name_plural = "Вложенные меню"

    def __str__(self):
        return f"{self.name}"
