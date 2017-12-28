from budgetme.apps.core.renderers import BudgetMeJSONRenderer


class TransactionJSONRenderer(BudgetMeJSONRenderer):
    object_label = 'transaction'
    pagination_object_label = 'transactions'
