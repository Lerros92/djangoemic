from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm, AddItemForm

# Create your views here.
def index(request):
    return render(request, 'baohanh/index.html')

def addnote(request):
    if request.method == "POST":
        pass
    else:
        form = AddForm()
        return render(request, "baohanh/addnote_page.html", {"form": form})

def additem(request):
    if request.method == "POST":
        pass
    else:
        form = AddItemForm()
        return render(request, "baohanh/additem_page.html", {"form": form})