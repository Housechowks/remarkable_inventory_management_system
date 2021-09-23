from typing import DefaultDict
from django.db import models

# Create your models here.
#in this case my products will be trucks 

class Delivery_Note(models.Model):
    contract_job = models.CharField(max_length=20, blank= True)
    material_type = models.CharField(max_length=12)
    delivery_number = models.IntegerField(blank=True)
    plate_number = models.CharField(max_length= 12)
    Date_delivered =models.DateField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    tonnages = models.FloatField(help_text='tons ')
    material_source = models.CharField(max_length=20)
    material_destination =models.CharField(max_length=12)



##this string rep product and date created
    def __str__(self):
        return f" Contract: {self.contract_job} - Vehicle Reg. : {self.plate_number} - Del No. {self.delivery_number} - net tons : {self.tonnages} - source : {self.material_source} - destination : {self.material_destination} - delivered on : {self.Date_delivered.strftime('%d/%m/%y')} - created on: {self.created.strftime('%d/%m/%y')}"

