from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm, AddItemForm
from .models import receiveTable, item

# Create your views here.
def index(request):
    items = item.objects.all()
    return render(request, "baohanh/all_items.html",{"items": items})

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

def notedetail(request, note_id):
    try:
        noteNumber = receiveTable.objects.get(id=note_id)
        items = noteNumber.item.all()
        context = {
            "noteNumber": noteNumber,
            "items": items,
        }
        return render(request, "baohanh/note_detail.html", context)
    except:
        return HttpResponse("Khong co phieu tiep nhan nay")