from rest_framework import serializers
from product.models import Product, UserProduct, Lesson, UserLesson


class LessonSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    watching_time = serializers.SerializerMethodField()

    class Meta:
        fields = ("name", "video_url", "duration", "status", "watching_time")
        model = Lesson

    def get_status(self, obj):
        user = self.context.get("request").user
        try:
            user_lesson = UserLesson.objects.get(user=user, lesson=obj)
            return user_lesson.status
        except UserLesson.DoesNotExist:
            return None

    def get_watching_time(self, obj):
        user = self.context.get("request").user
        try:
            user_lesson = UserLesson.objects.get(user=user, lesson=obj)
            return user_lesson.watching_time
        except UserLesson.DoesNotExist:
            return None

class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        fields = ("name", "owner", "lessons")
        model = Product


class UserProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        fields = ("user", "product")
        model = UserProduct


class UserLessonSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("user", "lesson", "watching_time", "status")
        model = UserLesson