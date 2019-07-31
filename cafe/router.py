from rest_framework import routers
from .views import SnackViewSet, ReportViewSet


cafe_router = routers.SimpleRouter()
cafe_router_order = routers.SimpleRouter()

cafe_router.register(r'snacks', SnackViewSet)
cafe_router.register(r'report', ReportViewSet)
cafe_router_order.register(r'order', SnackViewSet)

