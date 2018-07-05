from django.db import models

# Create your models here.
class Logger(models.Model):
    idKey = models.CharField(max_length=100)
    slug = models.SlugField()
    temp = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.idKey
