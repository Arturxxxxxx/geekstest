from django.db import models

class Product(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    completed = models.BooleanField(default=False, verbose_name='вналичии')
    created = models.DateTimeField(auto_now_add=True)

