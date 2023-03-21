from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.name
class Info(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    address = models.TextField(max_length=162)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pay = models.CharField(max_length=80)
    date = models.DateField()

    def __str__(self) -> str:
        return self.name
