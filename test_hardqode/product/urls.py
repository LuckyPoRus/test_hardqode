from django.urls import path

from product.views import ProductStatisticViewSet

urlpatterns = [
    path(
        "product-statistic/",
        ProductStatisticViewSet.as_view({"get": "list"})
    ),
]
