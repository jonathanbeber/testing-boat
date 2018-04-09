from django.shortcuts import render, redirect

from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item(text=request.POST['new-item']).save()
        return redirect('/list/the-only-existing-list')
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
