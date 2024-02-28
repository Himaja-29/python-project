from django.db import models

# Create your models here.
class himaja(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
class Meta:
    db_table="himaja"

#
# class sharu(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField(primary_key=True)
#     phonenumber=models.IntegerField()
#     suggestions=models.CharField(max_length=200)
#
#     class Meta:
#         db_table="sharu"

class Feedbackform(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    feedback_message=models.TextField()

    class Meta:
        db_table = 'Feedbackform'
