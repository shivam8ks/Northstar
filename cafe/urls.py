from django.urls import path
from django.conf.urls import include
from cafe import router

urlpatterns = [
    path(r'rest/v1/', include(router.cafe_router.urls)),
    path(r'user/', include(router.cafe_router_order.urls)),
]

