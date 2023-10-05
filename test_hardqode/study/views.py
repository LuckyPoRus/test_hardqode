from django.db.models import Q, F, FilteredRelation
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from product.models import ProductAccess
from study.models import Lesson
from study.serializers import MyLessonsSerializer


class MyLessonsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = MyLessonsSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        accesses = ProductAccess.objects.filter(
            user=self.request.user,
            is_valid=True
        )

        qs = Lesson.objects.filter(
            products__in=accesses.values("product_id")
        ).alias(
            view_info=FilteredRelation(
                "views",
                condition=Q(views__user=self.request.user)
            )
        ).annotate(
            status=F("view_info__status"),
            view_time=F("view_info__view_time")
        )
        return qs
