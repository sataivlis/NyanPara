from django.db import models
from django.conf import settings
from django.utils import timezone

class Cat(models.Model):
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    img_url = models.CharField(max_length=300)

    def __str__(self):
        return self.color + " " + self.breed

class UserCat(models.Model):
    cat_id = models.ForeignKey(Cat, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    birthdate = models.DateTimeField(default=timezone.now) #is timezone.now a function? not too sure
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname + "belonging to " + owner.name
