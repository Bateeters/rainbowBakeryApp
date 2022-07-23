from django.shortcuts import render
from django.utils import timezone
from .models import Item

# Create your views here.


def item_list(request):
    items = Item.objects.filter(save_date__lte=timezone.now()).order_by('name')
    return render(request, 'app/item_list.html', {'items': items})
