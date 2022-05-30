from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import Rate


class RateSerializer(serializers.ModelSerializer):
    group = serializers.CharField(max_length=25, required=True)
    rate = serializers.IntegerField(required=True)
    currency = serializers.CharField(max_length=10, required=True)

    class Meta:
        model = Rate
        fields = ('group', 'rate', 'currency')

    def create(self, validated_data):
        group = Group.objects.get(name=validated_data['group'])
        try:
            user_rate = Rate.objects.get(group=group, currency=validated_data['currency'])
            user_rate.rate = validated_data['rate']
            user_rate.save()
        except Rate.DoesNotExist:
            user_rate = Rate.objects.create(group=group, rate=validated_data['rate'],
                                            currency=validated_data['currency'])
        return user_rate
