from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) #takes timestamp only once, when CREATED

    def __str__(self) -> str:
        return self.body[0:50]