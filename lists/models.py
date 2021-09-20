from django.db import models

# Create your models here.
class List(models.Model):

    todo = models.CharField(max_length=100)

    def __str__(self):
        return self.todo