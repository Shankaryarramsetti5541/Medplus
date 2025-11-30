from django.db import models
from django.db.models import Model
class register(models.Model):
    id=models.CharField(primary_key=True)
    Customername=models.CharField()
    Gender=models.CharField()
    DateOfBirth=models.DateField()
    Phonenumber=models.IntegerField()
    Email=models.EmailField()
    State=models.CharField()
    City=models.CharField()
class operat(models.Model):
    OID=models.IntegerField(primary_key=True)
    OName=models.CharField()
    OUsername=models.CharField()
    Password=models.CharField()
    Gender =models.CharField()
    Phone=models.IntegerField()
class medicin(models.Model):
    MedicineID=models.IntegerField(primary_key=True)
    MedicineName=models.CharField()
    EXPDate=models.DateField()
    ProductCost=models.IntegerField()
    SeellingCost=models.IntegerField()
    Availability=models.IntegerField()
    Image=models.FileField()
class Transaction(models.Model):
    TransactionID=models.IntegerField(primary_key=True)
    Date=models.CharField()
    Cusid=models.CharField()
    MID=models.IntegerField()
    OperatorID=models.IntegerField()
    Quantity=models.IntegerField()
    BillAmount=models.IntegerField()