from django import template

register = template.Library()

@register.filter(name="draw_menu")
def draw_menu(name):
    ...
