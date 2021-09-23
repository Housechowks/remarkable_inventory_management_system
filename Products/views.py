from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Delivery_Note

def home_view(request):
    hello = 'hello mf'
    return render (request, 'Products/home.html' , {'h' : hello})

class SaleListView( ListView):
    model = Delivery_Note
    template_name = 'Products/main.html'    


class SaleDetailView(DetailView):
    model = Delivery_Note
    template_name = 'Products/detail.html'

def sale_list_view(request):
    qs = Delivery_Note.objects.all()
    return render (request, 'Products/main.html', {'object_list' : qs})

def sale_detail_view(request, **kwargs):
    pk = kwargs.get('pk')
    obj = Sale.objects.get(pk=pk)
    return render(request, 'Products/detail.html',{'object':obj})
