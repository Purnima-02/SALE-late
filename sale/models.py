from django.db import models

# Create your models here.



class SALE(models.Model):

    dsa_registerid=models.CharField(max_length=100)
    dsa_name=models.CharField(max_length=100)
    dsa_password=models.CharField(max_length=200,null=True,blank=True)


class SALE_Applications(models.Model):
    dsa=models.ForeignKey(SALE, on_delete=models.CASCADE, related_name='dsa',blank=True,null=True)
    cust_applicationId=models.CharField(max_length=100)
    # loan_type=models.CharField(max_length=100,null=True)


