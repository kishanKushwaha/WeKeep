from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True,null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

class product(models.Model):
    item_name = models.CharField(max_length=30,default='NULL')
    price = models.FloatField(default='NULL')
    brand = models.CharField(max_length=30,default='NULL')
    model = models.CharField(max_length=50,default='NULL')
    type = models.CharField(max_length=50,default='NULL')
    date = models.DateField(default='0000-00-00')
    invoice_image = models.ImageField(default='NULL')
    Warranty = models.BooleanField(default='NULL')
    duration_warranty = models.IntegerField(default='NULL')
    Is_Alert_Needed = models.BooleanField(default='NULL')
    Insurance = models.BooleanField(default='NULL')
    duration_insurance = models.IntegerField(default='NULL')
