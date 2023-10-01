from django.contrib import admin

from .models import Product, UserProduct, Lesson, UserLesson


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner"
    )


class UserProductAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product"
    )


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "video_url",
        "duration",
        "get_products"
    )

    @admin.display(description="Продукты")
    def get_products(self, obj):
        return ', '.join([p.name for p in obj.products.all()])


class UserLessonAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "lesson",
        "watching_time",
        "status"
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(UserProduct, UserProductAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(UserLesson, UserLessonAdmin)