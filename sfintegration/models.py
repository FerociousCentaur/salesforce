from django.db import models

# Create your models here.
class Contacts(models.Model):
    sd_id = models.CharField(max_length=30,blank=True,null=True)
    f_name = models.CharField(max_length=20,blank=True)
    l_name = models.CharField(max_length=20,blank=True)


