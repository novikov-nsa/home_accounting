from django.shortcuts import render
from .models import Accounts, Orginfo, Operations

# Create your views here.
def main_app(request):
    latest_oper = Operations.objects.order_by('dateOper')[:5]
    context = {'latest_oper': latest_oper}
    return render(request, 'main.html', context)