from django.shortcuts import render
from .models import Item


def index(request):
    itens = Item.objects.all()
    template = 'core/index.html'
    context = {'itens': itens}

    return render(request, template, context)

