from django.contrib import admin
from .models import Operations, Orginfo, Accounts, AccountsOrg

admin.site.register(Operations)
admin.site.register(Orginfo)
admin.site.register(Accounts)
admin.site.register(AccountsOrg)

# Register your models here.
