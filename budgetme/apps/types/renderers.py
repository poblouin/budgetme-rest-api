from budgetme.apps.core.renderers import BudgetMeJSONRenderer


class TransactionCategoryJSONRenderer(BudgetMeJSONRenderer):
    object_label = 'transaction_category'
    pagination_object_label = 'transaction_categories'
