from django.db import models

# Create your models here.


class List(models.Model):
    text = models.CharField(max_length=200)
    list_order = models.IntegerField()

    def __str__(self):
        return self.text
