from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Add(models.Model):
    header = models.CharField(max_length=100, null=True, blank=True)
    add_id = models.PositiveIntegerField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(null=False, default=0)
    position = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f'{self.position}. Заголовок: {self.header} Автор: {self.author} id:{self.add_id}'

    class Meta:
        indexes = [
            models.Index(fields=['-views']),
        ]
        ordering = ['-views']
