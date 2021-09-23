from django.db import models


class Task(models.Model):
    title = models.CharField('title', max_length=50)
    text = models.TextField('text')

    def __str__(self):
        return self.title

