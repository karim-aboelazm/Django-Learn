from django.db import models
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="post created at",null=True)
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

class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.TextField()
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.post.pk})
    
    class Meta:
        verbose_name_plural = "Comments"
    def __str__(self):
        return f"comment number ({self.id}) for post number ({self.post.id})"

class CommentsReply(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    reply = models.TextField()
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.post.pk})
    
    class Meta:
        verbose_name_plural = "Comments Reply"
    def __str__(self):
        return f"comment reply number ({self.id}) for comment with title ({self.comment.comment})"
    
class PostReact(models.Model):
    REACTS = ((str(i),str(i)) for i in ['LIKE','LOVE','SAD','CARE'])
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    post_react = models.CharField(max_length=10,choices=REACTS,default='LIKE')
    class Meta:
            verbose_name_plural = "Post React"
    def __str__(self):
        return f"Post number ({self.post.id}) has reacted with ({self.post_react})"