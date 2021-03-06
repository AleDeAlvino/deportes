from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    def __str__(self):
        return "{} {}".format(self.user, self.desc)