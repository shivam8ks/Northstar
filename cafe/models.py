from django.db import models
import datetime
from django.utils import timezone


class snacks(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    is_active = models.BooleanField(default=False)


# class menu(models.Model):
#     snack_id = models.ForeignKey(snacks.pk)
#     date_time = models.DateField(default=datetime.date.today)


class cart(models.Model):
    emp_id = models.IntegerField(null=True)
    cart_id = models.IntegerField(null=True)
    snack_id = models.IntegerField(null=True)
    qty = models.IntegerField(null=True)
    date_time = models.DateField(default=datetime.date.today)
    total = models.FloatField(null=True)
    payment_status = models.CharField(max_length=50)
    txn_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "Employee id: " + str(self.emp_id) + " and total: " + str(self.total)

