from django.db import models


class Categories(models.Model):
    Cateogry_name = models.CharField(max_length=50)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Cateogry_name}"


class Sub_Categories(models.Model):
    subCategory_name = models.CharField(max_length=50)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(default=1)
    isFeautred = models.PositiveIntegerField(null=True, blank=True)
    setPriorty = models.PositiveIntegerField(null=True, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateField(null=True)

    def __str__(self):
        return f"{self.subCategory_name}"


class Products(models.Model):
    product_name = models.CharField(max_length=60)
    product_short_description = models.TextField(max_length=100)
    product_description = models.TextField()
    product_price = models.IntegerField()
    product_sale_price = models.PositiveIntegerField(null=True, blank=True)
    product_upload_date = models.DateField()
    product_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_subcategory = models.ForeignKey(Sub_Categories, on_delete=models.CASCADE)
    product_status = models.PositiveIntegerField(null=True, blank=True)
    isFeatured = models.PositiveIntegerField(null=True, blank=True)
    priorty = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.product_name} - {str(self.product_category)} - {str(self.product_subcategory)}"


class Product_Images(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_images')
    product_Image = models.ImageField(upload_to="shop/images")


class Home_Slider(models.Model):
    slider_heading = models.CharField(max_length=100)
    slider_text = models.CharField(max_length=255)
    slider_Image = models.ImageField(upload_to="shop/slider_images")
    slider_priorty = models.PositiveIntegerField(null=True, blank=True)
    slide_link = models.TextField(null=True)

    def __str__(self):
        return f"{self.slider_heading}"

class Qoutes(models.Model):
    qoute = models.TextField()
    auther = models.CharField(max_length=55)
    forDate = models.DateField()

    def __str__(self):
        return f"{self.qoute} - {self.auther} "

class BestSelling(models.Model):
    Product_id = models.ForeignKey(Products , on_delete=models.CASCADE)
    status = models.IntegerField(null=True)
    Added_Dated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Product_id} - {self.status} {self.Added_Dated}"

