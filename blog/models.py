from django.db import models

# Create your models here.
class BlogModel(models.Model):
    judul = models.CharField(max_length=20)
    body = models.TextField()
    category = models.CharField(max_length=20)
def __str__ (self):
    return "{}.{}".format(self.id, self.judul)
