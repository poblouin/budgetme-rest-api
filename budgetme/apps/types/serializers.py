
from rest_framework import serializers

from budgetme.apps.types.models import TransactionCategory


class TransactionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionCategory
        fields = (
            'id',
            'name',
            'transaction_type',
        )
        extra_kwargs = {
            'name': {'validators': []},
        }

    def create(self, validated_data):
        user = validated_data.pop('user')

        return TransactionCategory.objects.create(
            user=user, **validated_data
        )

    def validate(self, data):
        """
        Needed to bypass the unique constraint validation for the name, otherwise the nested serializers won't work.
        """
        if type(self.context['view']).__name__ != 'TransactionCategoryViewSet':
            return data

        try:
            TransactionCategory.objects.get(user=self.context['request'].user,
                                            name=data['name'],
                                            transaction_type=data['transaction_type'])
        except TransactionCategory.DoesNotExist:
            pass
        else:
            raise serializers.ValidationError('A transaction category with this name already exists.')
        return data
