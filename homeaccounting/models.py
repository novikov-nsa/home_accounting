from django.db import models

# Create your models here.

class Accounts(models.Model): #Счета учета
    accountCode = models.CharField(max_length=20)
    accountName = models.CharField(max_length=200)
    accountTypeCode = models.CharField(max_length=2) #код типа счета 01 - фин.актив 02- доход
                                                     # 03- Дт задолженность 04- Кт задолженность

class Operations(models.Model): #операции
    dateOper = models.DateField()
    nameOper = models.CharField(max_length=200)
    accountDtOper = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    accountKtOper = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    sumOper = models.DecimalField(max_digits=20, decimal_places=2)


