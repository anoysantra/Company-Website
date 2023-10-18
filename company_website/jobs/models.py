from django.db import models

# Create your models here.
from django.db import models


class JobPost(models.Model):
    name = models.CharField(max_length=100)
    job_title= models.CharField(max_length=20, primary_key= True)
    company_name=models.CharField(max_length=30)
    company_email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    job_description= models.TextField()

    def __str__(self):
        return self.job_title
    

class Consultant(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    phone_number=models.BigIntegerField()
    comment=models.TextField()

    def __str__(self):
        return self.name
    
