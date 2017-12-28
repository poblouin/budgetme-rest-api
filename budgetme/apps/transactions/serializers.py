from rest_framework import serializers

from budgetme.apps.transactions.models import Transaction
from budgetme.apps.types.models import TransactionCategory
from budgetme.apps.types.serializers import TransactionCategorySerializer


class TransactionSerializer(serializers.ModelSerializer):
    transaction_category = TransactionCategorySerializer()

    class Meta:
        model = Transaction
        fields = (
            'id',
            'amount',
            'date',
            'transaction_category',
        )

    def create(self, validated_data):
        user = validated_data.pop('user')
        transaction_category_data = validated_data.pop('transaction_category')
        try:
            transaction_category = TransactionCategory.objects.get(user=user, **transaction_category_data)
        except TransactionCategory.DoesNotExist:
            raise serializers.ValidationError('Please specify an existing transaction category.')

        return Transaction.objects.create(
            user=user,
            transaction_category=transaction_category,
            **validated_data
        )
