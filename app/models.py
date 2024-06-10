from django.db import models

# Create your models here.
class Add(models.Model):
    header = models.CharField(max_length=50, null=True, blank=True)
    add_id = models.PositiveIntegerField(null=False, unique=True)
    author = models.CharField(max_length=50)
    views = models.PositiveIntegerField(null=False)
    position = models.PositiveIntegerField(null=False)
    
    def __str__(self):
        return f'{self.position}. Заголовок: {self.header} Автор: {self.author} id:{self.add_id}'
