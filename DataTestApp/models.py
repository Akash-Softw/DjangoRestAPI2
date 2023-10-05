from django.db import models
class Book(models.Model):
    objects = None
    type = models.CharField(max_length=20)
    page_num = models.IntegerField()

    def __str__(self):
        return self.type






# Create your models here.
