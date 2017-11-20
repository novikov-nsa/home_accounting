from django.shortcuts import render
from .models import Accounts, Orginfo, Operations
from django.db.models import Sum
from django.views.generic import TemplateView
import datetime

# Create your views here.
class MainView(TemplateView):

    def get(self, request, *args, **kwargs):
        template_name = 'main.html'
        #latest_oper = Operations.objects.order_by('dateOper')
        latest_oper = list(Operations.objects.all().values('dateOper') \
            .annotate(sum_on_date=Sum('sumOper')).order_by('-dateOper'))
        for item_date in latest_oper:
            print(item_date['dateOper'])
            print('\n')
            list_oper_to_date = list(Operations.objects.filter(dateOper=item_date['dateOper'])\
                                                          .values('nameOper', 'accDtOper__accountCode',\
                                                                  'accDtOper__accountName', 'accKtOper__accountCode',\
                                                                  'accKtOper__accountName', 'sumOper'))
            print(list_oper_to_date)
            #latest_oper[item_date] =list(latest_oper[item_date], **list_oper_to_date)


        print(latest_oper)

        context = {'latest_oper': latest_oper}
        return render(request, template_name, context)