# myapi/urls.py
from django.urls import path
from .views import ChargeView, FinishChargeView

urlpatterns = [
    path('start-charging', ChargeView.as_view(), name='start_charge'),
    path('finish-charging', FinishChargeView.as_view(), name='finish_charge')
]
