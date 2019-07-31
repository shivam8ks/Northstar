from django.shortcuts import render
from .models import snacks, cart
from .serializers import SnackSerializer, CartSerializer
from rest_framework import viewsets


class SnackViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = snacks.objects.all()
    serializer_class = SnackSerializer


class ReportViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing orders.
    """
    queryset = cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned records to a given date range,
        by filtering against 'from_date and to_date' query parameter in the URL.
        """
        from_date = self.request.query_params.get('from_date', None)
        to_date = self.request.query_params.get('to_date', None)
        queryset = cart.objects.raw("select * from cafe_cart where date_time between "
                                    +from_date + " and " + to_date+" ;")

        return queryset

