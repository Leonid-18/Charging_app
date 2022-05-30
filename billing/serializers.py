from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import BillingItem
from .constants import BILLING_ITEM_TYPE_CHARGE
from payments.models import Rate


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingItem
        fields = ('identifier', 'currency', 'rate')

    def create(self, validated_data):
        request = self.context.get('request')
        user = User.objects.get(pk=request.user.id)
        group = Group.objects.get(user=request.user.id)
        user_rate = Rate.objects.get(group=group)
        # Here we have to connect with checkout system
        billing_item = BillingItem.objects.create(
            user=user,
            type=BILLING_ITEM_TYPE_CHARGE,
            currency=user_rate.currency,
            rate=user_rate.rate
        )

        billing_item.save()

        return billing_item
