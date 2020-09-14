from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.IntegerField(unique=True,auto_created=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    mobile=models.IntegerField(default=0)
    credit=models.IntegerField(default=0)
    previous_credit=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    history=models.TextField()
    def __str__(self):
        return self.history
