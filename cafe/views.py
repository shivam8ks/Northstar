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


class CartViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing orders.
    """
    queryset = cart.objects.all()
    serializer_class = CartSerializer

