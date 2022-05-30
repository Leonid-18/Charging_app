# myapi/urls.py
from django.urls import path
from .views import RateView, RetrieveRatesView

urlpatterns = [
    path('rate', RateView.as_view(), name='rate'),
    path('rates', RetrieveRatesView.as_view(), name='rates'),
]
