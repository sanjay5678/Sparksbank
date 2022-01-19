from django.db import models
from django.utils import timezone

# Create your models here.
class Transfers(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,null=True) 
    email=models.CharField(max_length=20,null=True)
    balance=models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)

class Transactions(models.Model):   
    id = models.AutoField(primary_key=True)
    fromName = models.CharField(max_length=50,null=True)
    toName = models.CharField(max_length=50,null=True)
    amount = models.IntegerField(null=True)
    date = models.DateTimeField(null=True,default=timezone.now())
    
    def __str__(self):
        return str(self.id)