from django.contrib import admin

from budgetme.apps.types.models import TransactionCategory, Budget

admin.site.register(Budget)
admin.site.register(TransactionCategory)
