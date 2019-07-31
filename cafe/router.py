from rest_framework import routers
from .views import SnackViewSet, CartViewSet


cafe_router = routers.SimpleRouter()
cafe_router.register(r'snacks', SnackViewSet)
cafe_router.register(r'cart', CartViewSet)

# urlpatterns = cafe_router.urls

