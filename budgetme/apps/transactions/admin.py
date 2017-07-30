from django.contrib import admin

from budgetme.apps.transactions.models import Account, Transaction

admin.site.register(Account)
admin.site.register(Transaction)
