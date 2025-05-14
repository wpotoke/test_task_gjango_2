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


class SubMenu(models.Model):

    main_menu = models.ForeignKey(MainMenu, on_delete=models.PROTECT, related_name="sub", verbose_name="Главное меню")
    name = models.CharField(max_length=100, unique=True, verbose_name="Вложенное меню")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")

    class Meta:
        db_table = "sub_menu"
        verbose_name = "Вложенное меню"
        verbose_name_plural = "Вложенные меню"

    def __str__(self):
        return f"{self.name}"