from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class ToDo(models.Model):
    category = models.ForeignKey(Category,
                                related_name='todos',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id', 'completed')
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'

    def __str__(self):
        return self.title
    
