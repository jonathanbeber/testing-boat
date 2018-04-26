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
    if request.method == 'POST':
        Item(text=request.POST['new-item'], list=list_).save()
        return redirect(f'/list/{list_.id}/')
    items = Item.objects.filter(list=list_)
    return render(
        request,
        'list.html',
        {'items': items, 'list': list_}
    )


def new_list(request):
    new_list = List.objects.create()
    item = Item(text=request.POST['new-item'], list=new_list)
    try:
        item.full_clean()
    except ValidationError:
        new_list.delete()
        return render(request, 'home.html', {'error': 'Invalid item description'})
    item.save()
    return redirect(f'/list/{new_list.id}/')
