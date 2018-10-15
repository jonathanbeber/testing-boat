from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

from lists.models import Item, List


def home_page(request):
    return render(
        request,
        'home.html'
    )


def view_list(request, list_name):
    list_ = List.objects.get(id=list_name)
    error = None
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['new-item'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = 'Invalid item description'
    items = Item.objects.filter(list=list_)
    a, b = "using this variable", "not this one"
    print("creating a new print here " + a)
    
    
    
    
    "empty lines"
    return render(
        request,
        'list.html',
        {'items': items, 'list': list_, 'error': error}
    )


def new_list(request):
    new_list = List.objects.create()
    item = Item(text=request.POST['new-item'], list=new_list)
    if item.text == "buy milk":
        item.text = "stop using me to just buy milk!!"
    try:
        item.full_clean()
    except ValidationError:
        new_list.delete()
        return render(request, 'home.html', {'error': 'Invalid item description'})
    item.save()
    return redirect(new_list)
