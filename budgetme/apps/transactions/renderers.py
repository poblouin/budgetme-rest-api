from budgetme.apps.core.renderers import BudgetMeJSONRenderer


class AccountJSONRenderer(BudgetMeJSONRenderer):
    object_label = 'account'
    pagination_object_label = 'accounts'


class TransactionJSONRenderer(BudgetMeJSONRenderer):
    object_label = 'transaction'
    pagination_object_label = 'transactions'
