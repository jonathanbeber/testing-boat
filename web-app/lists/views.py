from django.shortcuts import render, redirect

from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item(text=request.POST['new-item']).save()
        return redirect('/')
    return render(
        request,
        'home.html',
        {'items': Item.objects.all()}
    )
