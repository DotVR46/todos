from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, db_index=True)
    tel_number = models.CharField(max_length=12, blank=False, db_index=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return f'{self.name} - {self.tel_number}'
