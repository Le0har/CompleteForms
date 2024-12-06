from django.db import models


class Form(models.Model):
    name = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True)
    data = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.name