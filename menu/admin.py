from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent', 'url', 'named_url')
    list_filter = ('menu',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None or obj.parent is None:
            form.base_fields['parent'].queryset = MenuItem.objects.none()
        else:
            form.base_fields['parent'].queryset = MenuItem.objects.filter(menu=obj.menu).exclude(id=obj.id)
        return form


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
