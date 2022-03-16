from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.CharField(max_length=50,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=50, null=True)
    publisher = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    genre = models.CharField(max_length=100, null=True)
    selled = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
