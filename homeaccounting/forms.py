from django import forms

class NewDocForm(forms.Form):
    dateOper = forms.DateField(label='Дата операции', widget=forms.DateInput)
    nameOper = forms.CharField(label='Наименование операции', max_length=250)
    sumOper = forms.DecimalField(label='Сумма')
    accDtOper = forms.DecimalField