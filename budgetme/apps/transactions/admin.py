from django.contrib import admin

from budgetme.apps.transactions.models import Transaction, ScheduledTransaction

admin.site.register(Transaction)
admin.site.register(ScheduledTransaction)
