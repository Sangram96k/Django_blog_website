from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils.text import slugify

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Category(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
class Post(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Published'),
    )
    SECTION = (
        ('Popular', 'Popular'),
        ('Recent', 'Recent'),
        
    )

    
    title=models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
   
    meta_title = models.CharField(max_length=60, blank=True)  # Meta title field
    meta_description = models.CharField(max_length=160, blank=True)  # Meta description field
    meta_keywords = models.CharField(max_length=255, blank=True)  
    content = RichTextUploadingField(blank=True, null=True)
    slug=models.SlugField(max_length=500,null=True,blank=True,unique=True)
    status=models.CharField(choices=STATUS,max_length=100)
    section = models.CharField(choices=SECTION,max_length=200)
    Main_post = models.BooleanField(default=False)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    post_img=models.ImageField(upload_to='posts/', blank=True, null=True)
    author_img=models.ImageField(upload_to='author/', blank=True, null=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    schema_json = models.TextField(blank=True, null=True)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate slug
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])



class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment from {self.name} - {self.content[:20]}..."