from django.shortcuts import render, redirect

from lists.models import Item

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
    Item(text=request.POST['new-item']).save()
    return redirect('/list/the-only-existing-list')
