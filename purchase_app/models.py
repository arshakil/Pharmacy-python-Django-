from django.db import models
from manufacturer_app.models import Manufacturer
from medicine_app.models import Medicine
from datetime import datetime
# Create your models here.


class Purchase(models.Model):
    CHOICES=(
        ('cash','Cash'),
        ('card','Card'),
        ('bkash','Bkash')
    )
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=50)
    pyment_type = models.CharField(max_length=11,choices=CHOICES)
    details = models.TextField(blank=True,null=True)
    batch_id = models.CharField(max_length=50)
    expiry_date = models.DateTimeField(auto_now=False,)
    quantity = models.IntegerField(blank=True,null=True)
    item_information = models.CharField(max_length=50, help_text='only show manufacturer medicine')
    stock = models.CharField(max_length=50, blank=True,null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    

    def __str__(self):
        return self.invoice_no

   
