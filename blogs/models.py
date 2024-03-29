from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
    
STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published"),
)
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 50, unique = True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    featured_image = models.ImageField(upload_to = 'uploads/%Y/%m/%d')
    blog_body = models.TextField(max_length = 2000)
    short_description = models.TextField(max_length = 500)
    status = models.CharField(max_length = 30, choices = STATUS_CHOICES, default = "Draft")
    is_featured = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


class About(models.Model):
    about_title = models.CharField(max_length = 20)
    about_description = models.CharField(max_length = 500)

    def __str__(self):
        return self.about_title
    
    class Meta:
        verbose_name_plural = "About"

class SocialLinks(models.Model):
    link_title = models.CharField(max_length = 20)
    link_url = models.URLField(max_length = 100)

    def __str__(self):
        return self.link_title
    
    class Meta:
        verbose_name_plural = "SocialLinks"


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length = 250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.comment