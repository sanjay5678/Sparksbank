from django.db import models

# Create your models here.
class Transfers(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,null=True) 
    balance=models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)
    
    