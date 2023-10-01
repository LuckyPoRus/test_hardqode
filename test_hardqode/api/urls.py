from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, UserProductViewSet, LessonViewSet, UserLessonViewSet


app_name = "api"

router = DefaultRouter()
router.register('products', ProductViewSet, basename="products")
router.register('userproducts', UserProductViewSet, basename="userproducts")
router.register('lessons', LessonViewSet, basename="lessons")
router.register('userlessons', UserLessonViewSet, basename="userlessons")

urlpatterns = [
    path("", include(router.urls))
]
