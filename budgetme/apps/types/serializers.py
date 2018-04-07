import string

from rest_framework import serializers

from budgetme.apps.types.models import TransactionCategory, Budget


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = (
            'id',
            'name',
            'amount',
            'budget_frequency'
        )
        extra_kwargs = {
            'name': {'validators': []},
        }

    def create(self, validated_data):
        user = validated_data.pop('user')

        return Budget.objects.create(
            user=user, **validated_data
        )

    def validate(self, data):
        """
        Needed to bypass the unique constraint validation for the name, otherwise the nested serializers won't work.
        """
        if type(self.context['view']).__name__ != 'BudgetViewSet':
            return data

        if not validate_name(data['name']):
            raise serializers.ValidationError('This name contains invalid characters')

        try:
            BudgetSerializer._get_budget_or_raise(self.context['request'].user, **{'name': data['name']})
        except Budget.DoesNotExist:
            pass
        else:
            raise serializers.ValidationError('A budget with this name already exists.')
        return data

    @staticmethod
    def validate_budget_or_raise(user, **budget_data):
        try:
            return BudgetSerializer._get_budget_or_raise(user=user, **budget_data)
        except Budget.DoesNotExist:
            raise serializers.ValidationError('Please specify an existing budget.')

    @staticmethod
    def _get_budget_or_raise(user, **budget_data):
        return Budget.objects.get(user=user, **budget_data)


class TransactionCategorySerializer(serializers.ModelSerializer):
    budget = BudgetSerializer()

    class Meta:
        model = TransactionCategory
        fields = (
            'id',
            'name',
            'budget',
        )
        extra_kwargs = {
            'name': {'validators': []},
        }

    def create(self, validated_data):
        user = validated_data.pop('user')
        budget_data = validated_data.pop('budget')
        budget = BudgetSerializer.validate_budget_or_raise(user=user, **budget_data)

        return TransactionCategory.objects.create(
            user=user,
            budget=budget,
            **validated_data
        )

    def update(self, instance, validated_data):
        user = self.context['request'].user
        budget_data = validated_data.pop('budget')
        budget = BudgetSerializer.validate_budget_or_raise(user=user, **budget_data)

        instance.name = validated_data.get('name', instance.name)
        instance.budget = budget
        instance.save()
        return instance

    def validate(self, data):
        """
        Needed to bypass the unique constraint validation for the name, otherwise the nested serializers won't work.
        """
        if type(self.context['view']).__name__ != 'TransactionCategoryViewSet' or \
                self.context['view'].action == 'update':
            return data

        if not validate_name(data['name']):
            raise serializers.ValidationError('This name contains invalid characters')

        try:
            TransactionCategorySerializer._get_transaction_category_or_raise(user=self.context['request'].user, name=data['name'])
        except TransactionCategory.DoesNotExist:
            pass
        else:
            raise serializers.ValidationError('A transaction category with this name already exists.')
        return data

    @staticmethod
    def validate_transaction_category_or_raise(user, name):
        try:
            return TransactionCategorySerializer._get_transaction_category_or_raise(user, name)
        except TransactionCategory.DoesNotExist:
            raise serializers.ValidationError('Please specify an existing transaction category.')

    @staticmethod
    def _get_transaction_category_or_raise(user, name):
        return TransactionCategory.objects.get(user=user, name=name)


def validate_name(name):
    """
    Validate that the name (either budget or transaction category name) does not contain special chars.
    Fix a bug with the filters, name with '+' cause the filter to return nothing.
    """
    permitted_chars = set(
        string.ascii_letters +
        string.digits +
        string.whitespace +
        '-._\'"éÉèÈàÀ()[]/'
    )
    name_to_valid = set(name)
    return name_to_valid.issubset(permitted_chars)
