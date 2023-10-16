from rest_framework import serializers


class ProductStatisticSerializer(serializers.Serializer):
    title = serializers.CharField()
    lesson_view_count = serializers.IntegerField()
    total_view_time = serializers.IntegerField()
    total_users_on_product = serializers.IntegerField()
    purchasing_percent = serializers.FloatField()
