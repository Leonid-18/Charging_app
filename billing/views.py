from .serializers import BillingSerializer
from rest_framework import generics, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.utils import timezone
from .models import BillingItem
from .constants import BILLING_ITEM_TYPE_CHARGE, BILLING_ITEM_TYPE_FINISHED


class ChargeView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BillingSerializer

    def create(self, request, *args, **kwargs):
        try:
            BillingItem.objects.get(
                user=request.user,
                type=BILLING_ITEM_TYPE_CHARGE,
            )
        except BillingItem.DoesNotExist:
            response = super().create(request, *args, **kwargs)
            return Response({
                'status': 200,
                'message': 'Start charging',
                'data': response.data
            })
        return Response({"status": status.HTTP_409_CONFLICT,
                         "message": 'User is charging'})


class FinishChargeView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_request = BillingSerializer

    def post(self, request, *args, **kwargs):
        try:
            charging_item = BillingItem.objects.get(
                user=request.user,
                type=BILLING_ITEM_TYPE_CHARGE,
            )
        except BillingItem.DoesNotExist:
            return Response({"status": status.HTTP_501_NOT_IMPLEMENTED,
                             "message": 'User is not charging'})
        charging_item.type = BILLING_ITEM_TYPE_FINISHED
        charging_item.cancelled_at = timezone.now()
        charging_item.amount = -(charging_item.created_at - charging_item.cancelled_at)\
            .total_seconds()*charging_item.rate/3600
        charging_item.save()
        return Response({
            'status': 200,
            'message': 'Finish charging',
            'amount': charging_item.amount
        })
