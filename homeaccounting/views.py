from django.shortcuts import render
from .models import Accounts, Orginfo, Operations
from django.db.models import Sum
from django.views.generic import TemplateView, FormView, CreateView, View
import datetime
from .forms import NewDocForm
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


# Create your views here.
class MainView(LoginRequiredMixin, View):
    login_url = '/login/'
    #redirect_field_name = 'main-view'

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

class NewDocFormView(LoginRequiredMixin, CreateView):
    template_name = 'new_doc.html'
    #form_class = NewDocForm
    model = Operations
    fields = ['dateOper', 'nameOper', 'sumOper', 'accDtOper', 'accKtOper', 'org']

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "registration/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")
