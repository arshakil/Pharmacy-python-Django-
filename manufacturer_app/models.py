from django.db import models
from phone_field import PhoneField
from datetime import datetime


# Create your models here.

class Manufacturer(models.Model):
    m_name = models.CharField(max_length=100, help_text='manufacturer company name')
    m_phone = PhoneField(blank=True, help_text='Contact phone number')
    m_address = models.TextField(blank=True, null=True)
    m_details = models.TextField(blank=True, null=True)
    m_previous_blance = models.DecimalField(max_digits=12, decimal_places=2)
    m_date = models.DateTimeField(default=datetime.now(), blank=True)


    def __str__(self):
        return self.m_name
    
    




    


