from django.db import models

# Create your models here.
class MainMenu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Главное меню")

    class Meta:
        db_table = "main_menu"
        verbose_name = "Гланое меню"
        verbose_name_plural = "Главные меню"

    def __str__(self):
        return f"{self.name}"
