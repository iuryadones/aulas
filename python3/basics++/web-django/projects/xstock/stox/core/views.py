from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Item
from .forms import ContactForm 

# from django.core.mail import EmailMessage
# from django.shortcuts import redirect
# from django.template import Context
# from django.template.loader import get_template
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def index(request):
    itens = Item.objects.all()
    template = 'core/shop-homepage/index.html'
    context = {'itens': itens}

    return render(request, template, context)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.like = [1 for _ in range(item.like)]
    return render(request, 'core/shop-item/index.html', {'item': item})

def contact(request):
    template = 'core/shop-contact/index.html'

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['msg']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')

    context = {'form': form}
    return render(request, template, context)

