from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Post(models.Model):
    image = models.ImageField(upload_to='blog',default='blog/default.jpg')
    author =models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_required = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
        #verbose_name = 'پست'
        #verbose_name_plural = 'پست ها'

    def __str__(self):
        return " {} - {}".format(self.title,self.id)


    def snippets(self):
        return self.content[:100] + ' ...'

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=2100)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']
        #verbose_name = 'نظر'
        #verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.name




