from django.db import models
from django.core.exceptions import ValidationError


class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    named_url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name

    def clean(self):
        if self.parent == self:
            raise ValidationError("Элемент меню не может быть своим же родителем.")
        if self.parent and self.parent.menu != self.menu:
            raise ValidationError("Родительский элемент должен принадлежать тому же меню.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
