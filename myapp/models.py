from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    class Meta:
        verbose_name_plural = "Our Posts"
    def __str__(self):
        return f"Post with title : {self.title}"
    
class Customers(models.Model):
    GENDER = (
        ("male","male"),
        ("female","female"),
    )
    name    = models.CharField(max_length = 200,verbose_name="customer name")
    age     = models.SmallIntegerField(default=18,verbose_name="customer age")
    image   = models.ImageField(upload_to = "customers/",verbose_name="customer profile")
    gender  = models.CharField(max_length = 200,choices= GENDER, default="male",verbose_name="customer gender")
    email   = models.EmailField(verbose_name="customer email")
    join_at = models.DateTimeField(auto_now_add=True,verbose_name="customer join at")

    #-----> meta
    class Meta:
        verbose_name_plural = "Our Customers"
    #-----> str
    def __str__(self):
        return f"user wiht full name : {self.name}"
