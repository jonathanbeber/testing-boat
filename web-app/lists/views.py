from django.shortcuts import render, redirect

from lists.models import Item, List

def home_page(request):
    return render(
        request,
        'home.html'
    )


def view_list(request):
    return render(
        request,
        'list.html',
        {'items': Item.objects.all()}
    )

def new_item(request):
    new_item_list = List()
    new_item_list.save()
    Item(text=request.POST['new-item'], list=new_item_list).save()
    return redirect('/list/the-only-existing-list')
