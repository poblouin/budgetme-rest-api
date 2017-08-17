from rest_framework import serializers

from budgetme.apps.transactions.models import Account, Transaction
from budgetme.apps.types.models import TransactionCategory
from budgetme.apps.types.serializers import TransactionCategorySerializer


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'id',
            'name',
            'account_type',
        )
        extra_kwargs = {
            'name': {'validators': []},
        }

    def create(self, validated_data):
        user = validated_data.pop('user')

        return Account.objects.create(
            user=user, **validated_data
        )

    def validate(self, data):
        """
        Needed to bypass the unique constraint validation for the name, otherwise the nested serializers won't work.
        """
        if type(self.context['view']).__name__ != 'AccountViewSet':
            return data

        try:
            Account.objects.get(user=self.context['request'].user,
                                name=data['name'],
                                account_type=data['account_type'])
        except Account.DoesNotExist:
            pass
        else:
            raise serializers.ValidationError('An account with this name already exists.')
        return data


class TransactionSerializer(serializers.ModelSerializer):
    transaction_category = TransactionCategorySerializer()
    account = AccountSerializer()

    class Meta:
        model = Transaction
        fields = (
            'id',
            'amount',
            'date',
            'transaction_category',
            'account',
        )
        extra_kwargs = {'account': {'write_only': True}}

    def create(self, validated_data):
        user = validated_data.pop('user')
        transaction_category_data = validated_data.pop('transaction_category')
        account_data = validated_data.pop('account')
        transaction_category, created = TransactionCategory.objects.get_or_create(user=user, **transaction_category_data)
        account, created = Account.objects.get_or_create(user=user, **account_data)

        return Transaction.objects.create(
            user=user,
            account=account,
            transaction_category=transaction_category,
            **validated_data
        )
