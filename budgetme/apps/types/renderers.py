from budgetme.apps.core.renderers import BudgetMeJSONRenderer


class BudgetJSONRenderer(BudgetMeJSONRenderer):
    object_label = 'budget'
    pagination_object_label = 'budgets'


class TransactionCategoryJSONRenderer(BudgetMeJSONRenderer):
    object_label = 'transaction_category'
    pagination_object_label = 'transaction_categories'
