from rest_framework import serializers
from .models import snacks, cart


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = snacks
        fields = ('id', 'name', 'price', 'is_active')
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = ('emp_id', 'cart_id', 'snack_id', 'qty', 'date_time', 'total', 'payment_status')
        fields = '__all__'

