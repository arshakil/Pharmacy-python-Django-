from django.db import models
from manufacturer_app. models import Manufacturer

# Create your models here.


class Category(models.Model):
   cat_name = models.CharField(max_length=100)
   date = models.DateTimeField( auto_now_add=True)

   def __str__(self):
        return self.cat_name
   
#    class Meta:
#        verbose_name = _("Category")
#        verbose_name_plural = _("Categorys")



    

class MedicineType(models.Model):
    type_name = models.CharField(max_length=100)
    

    # class Meta:
    #     verbose_name = _("MedicineType")
    #     verbose_name_plural = _("MedicineTypes")


    def __str__(self):
        return self.type_name

class Unit(models.Model):
    unit_name = models.CharField(max_length=50)

    

    # class Meta:
    #     verbose_name = _("Unit")
    #     verbose_name_plural = _("Units")

    def __str__(self):
        return self.unit_name




class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    strenght = models.CharField(max_length=25,blank=True, null=True)
    generic_name = models.CharField(max_length=100)
    box_size = models.CharField(max_length=50)
    medicine_shelf = models.CharField(max_length=25, blank=True, null=True)
    medicine_type = models.ForeignKey("MedicineType", on_delete=models.CASCADE)
    medicine_category = models.ForeignKey("Category",on_delete=models.CASCADE)
    menufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    unit = models.ForeignKey("Unit",on_delete=models.CASCADE)
    medicine_detail= models.TextField(blank=True, null=True)
    medicine_image = models.ImageField( upload_to='medicine_img/', blank=True, null=True)
    sell_price = models.DecimalField( max_digits=10, decimal_places=2)
    vat = models.CharField(max_length=10, blank=True, null=True)
    menufacturer_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField( auto_now_add=True)



    

    # class Meta:
    #     verbose_name = _("Medicine")
    #     verbose_name_plural = _("Medicines")

    def __str__(self):
        return self.medicine_name

    def get_absolute_url(self):
        return reverse("Medicine_detail", kwargs={"pk": self.pk})

