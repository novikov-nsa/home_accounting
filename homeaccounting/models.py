from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Accounts(models.Model): #Счета учета
    accountCode = models.CharField(max_length=20, primary_key=True)
    accountSegment1 = models.CharField(max_length=1)
    accountSegment2 = models.CharField(max_length=1)

    """
    Сегмент1 - код счета
    коды счетов:
    1 - денежные средства
    2 - расходы
    3- обязательства
    4- доходы
    5- дебиторская задолженность
    
    Сегмент 2- код субсчета
    задается для каждого счета, присутсвует в базовой поставке для всех пользователей
    """
    accountName = models.CharField(max_length=200)
    accountTypeCode = models.CharField(max_length=2) #код типа счета 01 - фин.актив 02- доход
                                                     # 03- Дт задолженность 04- Кт задолженность
                                                     # 05 - расход
class AccountsOrg(models.Model):
    accountCode = models.CharField(max_length=4, primary_key=True)
    org = models.ForeignKey("Orginfo", on_delete=models.CASCADE)
    accountBaseCode = models.ForeignKey(Accounts)
    accSegAnalit = models.CharField(max_length=2)
    accountName = models.CharField(max_length=200)

class Orginfo(models.Model):
    orgId = models.CharField(max_length=36, primary_key=True)
    orgName = models.CharField(max_length=200)

class Operations(models.Model): #операции
    org = models.ForeignKey(Orginfo, on_delete=models.CASCADE)
    dateOper = models.DateField()
    nameOper = models.CharField(max_length=200)
    accDtOper = models.ForeignKey(AccountsOrg, related_name="account_dt")
    accKtOper = models.ForeignKey(AccountsOrg, related_name="account_kt")
    sumOper = models.DecimalField(max_digits=20, decimal_places=2)

    def get_absolute_url(self):
        return reverse('main-view')




