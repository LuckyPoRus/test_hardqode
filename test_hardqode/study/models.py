from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product


User = get_user_model()


class Lesson(models.Model):
    title = models.CharField(max_length=32)
    video_url = models.URLField()
    video_duration = models.IntegerField(default=0)
    products = models.ManyToManyField(Product)


class LessonStatusEnum(models.TextChoices):
    VIEWED = "VIEWED"
    NOT_VIEWED = "NOT_VIEWED"


class LessonViewInfo(models.Model):
    lesson = models.ForeignKey(Lesson, models.CASCADE, "views")
    user = models.ForeignKey(User, models.CASCADE)
    status = models.CharField(
        choices=LessonStatusEnum.choices,
        default=LessonStatusEnum.NOT_VIEWED,
        max_length=32
    )
    view_time = models.IntegerField(default=0)

    class Meta:
        unique_together = ("lesson", "user")
