from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Product(models.Model):
    name = models.CharField(
        "Название продукта",
        max_length=255
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец продукта"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class UserProduct(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт"
    )

    class Meta:
        verbose_name = "Продукт пользователя"
        verbose_name_plural = "Продукты пользователя"

    def __str__(self):
        return f"У пользователя {self.user} есть доступ к {self.product}"


class Lesson(models.Model):
    name = models.CharField(
        "Название урока",
        max_length=255
    )
    video_url = models.URLField(
        "Ссылка на видео"
    )
    duration = models.PositiveIntegerField(
        "Длительность просмотра"
    )
    products = models.ManyToManyField(
        Product,
        related_name="lessons",
        verbose_name="Список продуктов"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name


class UserLesson(models.Model):
    WATCH_STATUS = [
        ("Watched", "Просмотрено"),
        ("Not watched", "Не просмотрено"),
        ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Урок"
    )
    watching_time = models.PositiveIntegerField(
        "Время просмотра"
    )
    status = models.CharField(
        "Статус просмотра",
        max_length=50,
        choices=WATCH_STATUS
    )

    class Meta:
        verbose_name = "Урок пользователя"
        verbose_name_plural = "Уроки пользователя"

    def __str__(self):
        return f"{self.lesson} {self.user}"

    def save(self, *args, **kwargs):
        if self.watching_time > self.lesson.duration * 0.8:
            self.status = "Watched"
        else:
            self.status = "Not watched"
        super().save(*args, **kwargs)
