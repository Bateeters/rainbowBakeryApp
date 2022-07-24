from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Item
from .forms import ItemForm
from django.shortcuts import redirect

# Create your views here.


def item_list(request):
    items = Item.objects.filter(
        save_date__lte=timezone.now()).order_by('name').order_by('category')
    return render(request, 'app/item_list.html', {'items': items})


def item_detail(request, pk):
    items = Item.objects.filter(
        save_date__lte=timezone.now()).order_by('name').order_by('category')
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save_date = timezone.now()
            item.save()
            return redirect('/item/new/', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'app/item_edit.html', {'form': form, 'items': items})


def item_new(request):
    items = Item.objects.filter(
        save_date__lte=timezone.now()).order_by('name').order_by('category')
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save_date = timezone.now()
            item.save()
            return redirect('/item/new/', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'app/item_edit.html', {'form': form, 'items': items})


def item_edit(request, pk):
    items = Item.objects.filter(
        save_date__lte=timezone.now()).order_by('name').order_by('category')
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save_date = timezone.now()
            item.save()
            return redirect('/item/new/', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'app/item_edit.html', {'form': form, 'items': items})
