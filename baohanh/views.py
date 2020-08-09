from django.shortcuts import render, redirect
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
    if request.method == "POST":
        form = AddItemForm(request.POST)
        if form.is_valid():
            add_item = item()
            noteNumber = receiveTable.objects.get(id=note_id)
            # item.noteNumber = receiveTable.objects.get(pk=int(form.cleaned_data["noteNumber"]))
            add_item.noteNumber = noteNumber
            add_item.itemName = form.cleaned_data["itemName"]
            add_item.quantity = form.cleaned_data["quantity"]
            add_item.itemGroup = form.cleaned_data["itemGroup"]
            add_item.status = form.cleaned_data["status"]
            add_item.check = form.cleaned_data["check"]
            add_item.conclude = form.cleaned_data["conclude"]
            add_item.deadline = form.cleaned_data["deadline"]
            add_item.note = form.cleaned_data["note"]
            add_item.done = form.cleaned_data["done"]
            add_item.save()
            return redirect("baohanh:notedetail", note_id=note_id)
        else:
            # print(form)
            return HttpResponse("Form is not valid")
    else:
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

def add(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            note = receiveTable()
            note.noteNumber = form.cleaned_data["noteNumber"]
            note.customers = form.cleaned_data["customers"]
            note.note = form.cleaned_data["note"]
            note.save()
        return redirect("baohanh:notedetail", note_id=note.pk)
    return render(request, "baohanh/add.html")