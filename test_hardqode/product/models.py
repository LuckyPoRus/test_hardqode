from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=32)
    user = models.ForeignKey(User, models.PROTECT)


class ProductAccess(models.Model):
    user = models.ForeignKey(User, models.PROTECT)
    product = models.ForeignKey(Product, models.PROTECT, "accesses")
    is_valid = models.BooleanField(default=True)
