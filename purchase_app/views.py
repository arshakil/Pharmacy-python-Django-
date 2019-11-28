from django.shortcuts import render
from manufacturer_app.models import Manufacturer
from medicine_app.models import Medicine

from django.http import JsonResponse

# Create your views here.

def add_purchase(request):
    manufacturer_name = Manufacturer.objects.all()
    context={
        'manufacturer_name':manufacturer_name,
      
    }
    return render(request,'add_purchase.html',context)

def load_medicine(request):
    id = request.GET.get('manufacturer_id',)
    medicine_name =  list(Medicine.objects.all().values().filter(menufacturer__id__icontains=id))
    data =  dict()
    data['medicine_name'] = medicine_name
    return JsonResponse(data)

  