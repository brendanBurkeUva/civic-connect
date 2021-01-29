from django.db import models

# Create your models here.
class EmailTemp(models.Model):
    category = models.CharField(max_length=200)
    letter = models.TextField()
    approved = models.BooleanField(default=False)
    sender = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.letter

class Address(models.Model):
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.address
