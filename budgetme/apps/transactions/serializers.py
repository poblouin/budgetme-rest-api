import datetime

from rest_framework import serializers

from budgetme.apps.transactions.models import Transaction, ScheduledTransaction
from budgetme.apps.types.serializers import TransactionCategorySerializer, BudgetSerializer


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

        budget = BudgetSerializer.validate_budget_or_raise(user, **budget_data)
        budget_is_active_or_raise(budget)
        transaction_category = TransactionCategorySerializer.validate_transaction_category_or_raise(user, transaction_category_data['name'])

        return Transaction.objects.create(
            user=user,
            transaction_category=transaction_category,
            **validated_data
        )

    def update(self, instance, validated_data):
        user = self.context['request'].user
        transaction_category_data = validated_data.pop('transaction_category')
        budget_data = transaction_category_data.pop('budget')

        budget = BudgetSerializer.validate_budget_or_raise(user, **budget_data)
        budget_is_active_or_raise(budget)
        transaction_category = TransactionCategorySerializer.validate_transaction_category_or_raise(user, transaction_category_data['name'])

        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.description = validated_data.get('description', instance.description)
        instance.transaction_category = transaction_category
        instance.save()
        return instance


class ScheduledTransactionSerializer(serializers.ModelSerializer):
    transaction_category = TransactionCategorySerializer()

    class Meta:
        model = ScheduledTransaction
        fields = (
            'id',
            'amount',
            'description',
            'frequency',
            'start_date',
            'end_date',
            'transaction_category',
        )

    def create(self, validated_data):
        user = validated_data.pop('user')
        transaction_category_data = validated_data.pop('transaction_category')
        budget_data = transaction_category_data.pop('budget')

        budget = BudgetSerializer.validate_budget_or_raise(user, **budget_data)
        budget_is_active_or_raise(budget)
        transaction_category = TransactionCategorySerializer.validate_transaction_category_or_raise(user, transaction_category_data['name'])

        return ScheduledTransaction.objects.create(
            user=user,
            transaction_category=transaction_category,
            **validated_data
        )

    def update(self, instance, validated_data):
        user = self.context['request'].user
        transaction_category_data = validated_data.pop('transaction_category')
        budget_data = transaction_category_data.pop('budget')

        budget = BudgetSerializer.validate_budget_or_raise(user, **budget_data)
        budget_is_active_or_raise(budget)
        transaction_category = TransactionCategorySerializer.validate_transaction_category_or_raise(user, transaction_category_data['name'])

        instance.amount = validated_data.get('amount', instance.amount)
        instance.description = validated_data.get('description', instance.description)
        instance.frequency = validated_data.get('frequency', instance.frequency)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.transaction_category = transaction_category
        instance.save()
        return instance

    def validate(self, data):
        now = datetime.datetime.utcnow().date()
        if data['start_date'] < now:
            raise serializers.ValidationError('The start date of a scheduled transaction cannot be less than today\'s date.')

        if data.get('start_date') and data.get('end_date') and data['start_date'] > data['end_date']:
            raise serializers.ValidationError('The start date must be less than or equal the end date.')

        return data


def budget_is_active_or_raise(budget):
    if not (budget.start_date and budget.end_date):
        return

    now = datetime.datetime.utcnow().date()
    if not (budget.start_date <= now <= budget.end_date):
        raise serializers.ValidationError('Cannot assign a transaction to an inactive budget.')
