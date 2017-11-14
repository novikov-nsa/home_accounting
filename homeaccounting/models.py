from django.db import models

# Create your models here.

class Accounts(models.Model): #Счета учета
    accountCode = models.CharField(max_length=20, primary_key=True)
    accountName = models.CharField(max_length=200)
    accountTypeCode = models.CharField(max_length=2) #код типа счета 01 - фин.актив 02- доход
                                                     # 03- Дт задолженность 04- Кт задолженность
                                                     # 05 - расход

class Orginfo(models.Model):
    orgId = models.CharField(max_length=36, primary_key=True)
    orgName = models.CharField(max_length=200)

class Operations(models.Model): #операции
    orgOper = models.ForeignKey(Orginfo, on_delete=models.CASCADE)
    dateOper = models.DateField()
    nameOper = models.CharField(max_length=200)
    accDtOper = models.ForeignKey(Accounts, related_name="account_dt")
    accKtOper = models.ForeignKey(Accounts, related_name="account_kt")
    sumOper = models.DecimalField(max_digits=20, decimal_places=2)




