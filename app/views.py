from django.shortcuts import render
from django.utils import timezone
from .models import Item
from .forms import ItemForm
from django.shortcuts import redirect

# Create your views here.


def item_list(request):
    items = Item.objects.filter(
        save_date__lte=timezone.now()).order_by('name').order_by('category')
    return render(request, 'app/item_list.html', {'items': items})


def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save_date = timezone.now()
            item.save()
            return redirect('/', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'app/item_edit.html', {'form': form})
