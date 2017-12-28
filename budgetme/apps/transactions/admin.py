from django.contrib import admin

from budgetme.apps.transactions.models import Transaction

admin.site.register(Transaction)
