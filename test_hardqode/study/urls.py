from django.urls import path, include
from rest_framework.routers import SimpleRouter

from study.views import MyLessonsViewSet


router = SimpleRouter()
router.register("my-lessons", MyLessonsViewSet, "my-lessons")


urlpatterns = [
    path("", include(router.urls))
]
