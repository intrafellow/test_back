from django import template
from menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu': []}

    request = context['request']
    current_url = request.path

    def build_tree(parent):
        tree = []
        for item in parent.children.all():
            tree.append({
                'item': item,
                'children': build_tree(item),
                'active': current_url.startswith(item.url) if item.url else False,
            })
        return tree

    menu_items = MenuItem.objects.filter(menu=menu, parent__isnull=True)
    tree = []
    for item in menu_items:
        tree.append({
            'item': item,
            'children': build_tree(item),
            'active': current_url.startswith(item.url) if item.url else False,
        })

    return {'menu': tree}
