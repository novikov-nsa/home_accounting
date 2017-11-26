from django.shortcuts import render
from .models import Accounts, Orginfo, Operations
from django.db.models import Sum
from django.views.generic import TemplateView, FormView, CreateView, View
import datetime
from .forms import NewDocForm
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin



# Create your views here.
class MainView(AccessMixin, View):
    #login_url = ''
    redirect_field_name = 'main-view'



    def get(self, request, *args, **kwargs):

        template_name = 'main.html'
        #latest_oper = Operations.objects.order_by('dateOper')
        latest_oper = list(Operations.objects.all().values('dateOper') \
            .annotate(sum_on_date=Sum('sumOper')).order_by('-dateOper'))

        list_oper_to_date = list(Operations.objects.all()\
                                .values('dateOper', 'nameOper', 'accDtOper__accountCode',\
                                        'accDtOper__accountName', 'accKtOper__accountCode',\
                                        'accKtOper__accountName', 'sumOper'))

        url = AccessMixin.get_login_url(self)
        context = {'latest_oper': latest_oper, 'list_oper_to_date':list_oper_to_date, 'url':url}

        #username = request.POST['username']
        #password = request.POST['password']
        #user = authenticate(username=username, password=password)
        #print(user)
        return render(request, template_name, context)

class NewDocFormView(LoginRequiredMixin, CreateView):
    template_name = 'new_doc.html'
    #form_class = NewDocForm
    model = Operations
    fields = ['dateOper', 'nameOper', 'sumOper', 'accDtOper', 'accKtOper', 'org']
