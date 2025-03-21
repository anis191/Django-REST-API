from django.db import models

"""
Step to build an api:
1st --> Create Model
2nd --> Create Serializer
3rd --> Define ViewSet
4th --> Set Router
"""

# Create Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return self.name

# Create Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/images/',blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
