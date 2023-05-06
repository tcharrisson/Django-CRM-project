'''we will be creating the models here, this shows the start of the actual CRM software
'''
from django.db import models

class Record(models.Model):
    '''this here will create the mysql query and add the following to the mysql database'''
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
