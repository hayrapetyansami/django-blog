from django.db import models
from django.urls import reverse
from django.conf import settings

class Category(models.Model):
  name_hy = models.CharField(max_length=255, unique=True)
  name_ru = models.CharField(max_length=255, unique=True)
  name_en = models.CharField(max_length=255, unique=True)
  cat_slug = models.SlugField(max_length=255, unique=True)
  
  class Meta:
    ordering = ['-id']
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  def get_absolute_url(self):
    return reverse('category', kwargs={'cat_slug': self.cat_slug})

  def __str__(self):
    return self.cat_slug

class Tag(models.Model):
  name_hy = models.CharField(max_length=255, unique=True)
  name_ru = models.CharField(max_length=255, unique=True)
  name_en = models.CharField(max_length=255, unique=True)
  tag_slug = models.SlugField(max_length=255, unique=True)
  
  class Meta:
    ordering = ['-id']
    verbose_name = 'Tag'
    verbose_name_plural = 'Tags'

  def get_absolute_url(self):
    return reverse('tags', kwargs={'tag_slug': self.tag_slug})

  def __str__(self):
      return self.tag_slug

class Post(models.Model):
  title_hy = models.CharField(max_length=255)
  title_ru = models.CharField(max_length=255)
  title_en = models.CharField(max_length=255)
  content_hy = models.TextField()
  content_ru = models.TextField()
  content_en = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  post_slug = models.SlugField(max_length=255, unique=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='post_images/', blank=True, null=True)
  tags = models.ManyToManyField(Tag, blank=True)

  class Meta:
    ordering = ['-created_at']
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def get_absolute_url(self):
    return reverse('post', kwargs={'cat_slug': self.category.cat_slug, 'post_slug': self.post_slug})

  def __str__(self):
    return self.post_slug