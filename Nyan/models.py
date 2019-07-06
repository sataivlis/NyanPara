from django.db import models
from django.conf import settings
from django.utils import timezone

class Cat(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birth_date = models.DateTimeField(default=timezone.now) #is timezone.now a function? not too sure

    def __str__(self):
        return self.name
