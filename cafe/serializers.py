from rest_framework import serializers
from .models import snacks, cart


class SnackSerializer(serializers.ModelSerializer):
    """
    Class to serialize entries from table: "cafe_snacks"
    """
    class Meta:
        model = snacks
        fields = ('id', 'name', 'price', 'is_active')


class CartSerializer(serializers.ModelSerializer):
    """
        Class to serialize entries from table: "cafe_cart"
    """
    class Meta:
        model = cart
        fields = ('emp_id', 'cart_id', 'snack_id', 'qty', 'date_time', 'total', 'payment_status', 'emp_name', 'ind_total', 'snack_name')
