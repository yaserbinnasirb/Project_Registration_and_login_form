from django.db import models
class reglog(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=10,null=False)
    email = models.EmailField()
    mobileno = models.IntegerField(max_length=11)


