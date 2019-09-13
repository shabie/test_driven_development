from django.shortcuts import render, redirect
from lists.models import Item, List
import os
os.environ['CHAMPU'] = 'lala'


# Create your views here.
def home_page(request):
    champu = os.environ['CHAMPU']
    return render(request, 'home.html', {champu})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
