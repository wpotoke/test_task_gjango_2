from django import template
from menu.models import MenuItem

register = template.Library()

@register.inclusion_tag(filename="menu/main_menu.html", takes_context=True)
def draw_menu(context, name_menu):
    url = context["request"].path
    menu_items = MenuItem.objects.select_related("parent").filter(menu_name=name_menu)
    if not menu_items:
        return {}
    active = menu_items.filter(url=url).first()
    path = set()

    cur = active
    while cur:
        path.add(cur.id)
        cur = cur.parent
    
    tree = []
    dict_menu = {i.id: {'item': i, "children": []} for i in menu_items}

    for item in menu_items:
        if item.parent_id:
            dict_menu[item.parent.id]["children"].append(dict_menu[item.id])
        else:
            tree.append(dict_menu[item.id])

    return {
    "tree": tree,
    "open_path": path,
    "active_id": active.id if active else None
    }