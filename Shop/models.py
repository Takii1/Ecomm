from django.db import models

class Categories(models.Model):
    Cateogry_name = models.CharField(max_length=50)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Cateogry_name}"

class Sub_Categories(models.Model):
    subCategory_name = models.CharField(max_length=50)
    Category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateField(null = True)

    def __str__(self):
        return f"{self.subCategory_name}"


class Products(models.Model):
    product_name = models.CharField(max_length=60)
    product_short_description = models.TextField(max_length=100)
    product_description = models.TextField()
    product_price = models.IntegerField()
    product_upload_date = models.DateField()
    product_category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    product_subcategory = models.ForeignKey(Sub_Categories,on_delete=models.CASCADE)
    product_status = models.IntegerField()

    def __str__(self):
        return f"{self.product_name} - {str(self.product_category)} - {str(self.product_subcategory)}"

class Product_Images(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_Image = models.ImageField(upload_to="shop/images")
