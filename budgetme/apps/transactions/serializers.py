from rest_framework import serializers

from budgetme.apps.transactions.models import Transaction
from budgetme.apps.types.models import TransactionCategory, Budget
from budgetme.apps.types.serializers import TransactionCategorySerializer


class TransactionSerializer(serializers.ModelSerializer):
    transaction_category = TransactionCategorySerializer()

    class Meta:
        model = Transaction
        fields = (
            'id',
            'amount',
            'date',
            'description',
            'transaction_category',
        )

    def create(self, validated_data):
        user = validated_data.pop('user')
        transaction_category_data = validated_data.pop('transaction_category')
        budget_data = transaction_category_data.pop('budget')

        try:
            Budget.objects.get(user=user, **budget_data)
        except Budget.DoesNotExist:
            raise serializers.ValidationError('Please specify an existing budget.')
        try:
            transaction_category = TransactionCategory.objects.get(user=user, name=transaction_category_data['name'])
        except TransactionCategory.DoesNotExist:
            raise serializers.ValidationError('Please specify an existing transaction category.')

        return Transaction.objects.create(
            user=user,
            transaction_category=transaction_category,
            **validated_data
        )

    def update(self, instance, validated_data):
        user = self.context['request'].user
        transaction_category_data = validated_data.pop('transaction_category')
        try:
            transaction_category = TransactionCategory.objects.get(user=user, name=transaction_category_data['name'])
        except TransactionCategory.DoesNotExist:
            raise serializers.ValidationError('Please specify an existing transaction category.')

        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.description = validated_data.get('description', instance.description)
        instance.transaction_category = transaction_category
        instance.save()
        return instance
