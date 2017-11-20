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

        list_oper_to_date = list(Operations.objects.all()\
                                .values('dateOper', 'nameOper', 'accDtOper__accountCode',\
                                        'accDtOper__accountName', 'accKtOper__accountCode',\
                                        'accKtOper__accountName', 'sumOper'))

        context = {'latest_oper': latest_oper, 'list_oper_to_date':list_oper_to_date}
        return render(request, template_name, context)