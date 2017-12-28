from rest_framework import serializers

from budgetme.apps.types.models import TransactionCategory, Budget


class BudgetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Budget
        fields = (
            'id',
            'name',
            'weekly_amount',
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

        try:
            Budget.objects.get(user=self.context['request'].user,
                               name=data['name'],
                               weekly_amount=data['weekly_amount'])
        except Budget.DoesNotExist:
            pass
        else:
            raise serializers.ValidationError('A budget with this name already exists.')
        return data


class TransactionCategorySerializer(serializers.ModelSerializer):
    budget = BudgetSerializer(write_only=True)

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
        try:
            budget = Budget.objects.get(user=user, **budget_data)
        except Budget.DoesNotExist:
            raise serializers.ValidationError('Please specify an existing budget.')

        return TransactionCategory.objects.create(
            user=user,
            budget=budget,
            **validated_data
        )

    def validate(self, data):
        """
        Needed to bypass the unique constraint validation for the name, otherwise the nested serializers won't work.
        """
        if type(self.context['view']).__name__ != 'TransactionCategoryViewSet':
            return data

        try:
            TransactionCategory.objects.get(user=self.context['request'].user, name=data['name'])
        except TransactionCategory.DoesNotExist:
            pass
        else:
            raise serializers.ValidationError('A transaction category with this name already exists.')
        return data
