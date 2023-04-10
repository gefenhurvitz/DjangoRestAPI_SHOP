from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Represents a category of products.
    """

    name = models.CharField(max_length=255, unique=True, verbose_name="category name")

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Represents a product that can be purchased.
    """

    name = models.CharField(max_length=255, verbose_name="product name")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Represents a customer order.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s order #{self.pk}"


class OrderItem(models.Model):
    """
    Represents a single item within an order.
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in order #{self.order.pk}"
