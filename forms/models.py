from django.db import models


class Form(models.Model):
    name = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True)
    data = models.DateTimeField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name