from django.db import models
from datetime import datetime, timedelta
# Create your models here.

class receiveTable(models.Model):
    noteNumber = models.CharField(max_length=10, unique=True)
    customers = models.CharField(max_length=50)
    receiveDay = models.DateField(auto_now_add=True)
    note = models.TextField()

    def __str__(self):
        return f"{self.noteNumber}"

class item(models.Model):
    noteNumber = models.ForeignKey(receiveTable, on_delete=models.CASCADE, related_name="item")
    itemName = models.CharField(max_length=60)
    quantity = models.IntegerField(null=False)
    itemGroup = models.CharField(max_length=10)
    status = models.CharField(max_length=128, null=True)
    check = models.CharField(max_length=128, null=True)
    conclude = models.CharField(max_length=128, null=True)
    deadline = models.DateField(null=False, default=(datetime.now() + timedelta(days=2)).date())
    note = models.TextField()

    def __str__(self):
        return f"{self.noteNumber} - {self.itemName}"
