from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Item
from .forms import ContactForm 

def index(request):
    itens = Item.objects.all()
    template = 'core/shop-homepage/index.html'
    context = {'itens': itens}

    return render(request, template, context)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'core/shop-item/index.html', {'item': item})

def contact(request):
    form = ContactForm()
    context = {'form': form}
    template = 'core/shop-contact/index.html'
    return render(request, template, context)

