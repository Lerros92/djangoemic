from django.db import models
from datetime import datetime, timedelta
# Create your models here.

class receiveTable(models.Model):
    noteNumber = models.CharField(max_length=10, unique=True)
    customers = models.CharField(max_length=50)
    receiveDay = models.DateField(auto_now_add=True)
    note = models.TextField()

    def __str__(self):
        return f"{self.noteNumber} - {self.customers} - {self.receiveDay}"

class item(models.Model):
    group = [
        ("TIDAU24", "TI dầu 24kV"),
        ("TUDAU24","TU dầu 24kV"),
        ("TIKHO24I", "TI khô 24kV trong nhà"),
        ("TIKHO24O", "TI khô 24kV ngoài trời"),
        ("TIHT", "TI hạ thế"),
    ]
    noteNumber = models.ForeignKey(receiveTable, on_delete=models.CASCADE, related_name="item")
    itemName = models.CharField(max_length=60)
    quantity = models.IntegerField(null=False)
    itemGroup = models.CharField(max_length=10, choices=group)
    status = models.CharField(max_length=128, null=True)
    check = models.CharField(max_length=128, null=True)
    conclude = models.CharField(max_length=128, null=True)
    deadline = models.DateField()
    note = models.TextField(null=True)
    done = models.BooleanField(choices=[(True, "Xong"), (False, "Chưa xong")], default=False)
    #null=False, default=(datetime.now() + timedelta(days=2)).date()

    def __str__(self):
        return f"{self.itemName} -> {self.noteNumber}"
