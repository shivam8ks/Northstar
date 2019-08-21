from .models import snacks, cart
from .serializers import SnackSerializer, CartSerializer
from rest_framework import viewsets, response
from rest_framework.decorators import action


class SnackViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = snacks.objects.all()
    serializer_class = SnackSerializer
    """
    Updated the insertion and updation of records based on incoming json objects.
    """
    @action(detail=False, methods=['POST'])
    def bulk_create(self, request):
        d = request.data
        ob_list = self.serializer_class(d, many=True)
        out_list = []
        for i in ob_list.data:
            try:
                s = snacks.objects.get(name=i["name"], price__exact=i["price"])
                s.is_active = i["is_active"]
                s.save()
            except Exception as e:
                snacks.objects.create(name=i["name"], price=i["price"], is_active=i["is_active"])
        return response.Response(out_list)


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

        print(from_date, to_date)
        if from_date:
            pass
        if to_date:
            pass

        query_set = cart.objects.filter(date_time__range=[str(from_date), str(to_date)])
        # query_set2 = snacks.objects.filter(is_active=1)


        # sql = "select * from cafe_cart as c, cafe_snacks as s where c.snack_id=s.id and c.date_time between '"+from_date+"' and '"+to_date+"' and s.is_active=1;"
        #c.id, c.payment_status, c.cart_id, c.date_time, c.emp_id, c.qty, c.snack_id, s.name
        # query_set = cart.objects.raw(sql)




        return query_set


# url for testing
# http://127.0.0.1:8000/rest/v1/report/?from_date=2019-07-22&to_date=2019-07-31
