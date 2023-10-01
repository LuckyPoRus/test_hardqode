from rest_framework.viewsets import ModelViewSet
from product.models import Product, UserProduct, Lesson, UserLesson
from .serializers import ProductSerializer, UserProductSerializer, LessonSerializer, UserLessonSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserProductViewSet(ModelViewSet):
    queryset = UserProduct.objects.all()
    serializer_class = UserProductSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class UserLessonViewSet(ModelViewSet):
    queryset = UserLesson.objects.all().order_by("user")
    serializer_class = UserLessonSerializer
