from django.db import models
from django.db.models.deletion import CASCADE
from Products.models import Delivery_Note
from Customers.models import customer
from Profiles.models import TRUCK_OWNWER
from django.utils import timezone
from .utills import generate_code
from django.shortcuts import reverse

#position is an instance of sale, which in this case its a delivery which is unique to a trck owner 

class Position(models.Model):
    Product = models.ForeignKey(Delivery_Note, on_delete=CASCADE)
    tonnages = models.FloatField(blank=True, null=True)
    applicable_rate = models.PositiveIntegerField()
    created = models.DateField(blank=True)
    

    def save(self, *args, **kwargs):
        self.total_amount = self.Produt.tonnages * self.applicable_rate
        return super().save(*args, **kwargs)
    
    def get_sales_id(self):
        sale_obj = self.sale_set.first()
        return sale_obj.id

    def __str__(self):
        return f" id: {self.id}, Truck: {self.Product.plate_number}, Delivery No. : {self.Product.delivery_number}, Destination : {self.Product.material_destination}, tonnages:{self.tonnages} "

class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_amount = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(customer, on_delete=CASCADE)
    owner = models.ForeignKey(TRUCK_OWNWER, on_delete=models.CASCADE)
    created = models.DateField(blank=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f" total amnt  {self.total_amount}"
    
    def get_absolute_url(self):
        return reverse( 'Records:detail', kwargs = { 'pk' : self.pk} )

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
           self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_created=True)

    def __str__(self):
        return str(self.file_name)

