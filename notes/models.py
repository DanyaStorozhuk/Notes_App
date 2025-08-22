from django.db import models

# Create your models here.


class Note(models.Model):
    text = models.CharField(max_length=300)
    title = models.TextField()

    def __str__(self):
        return self.text