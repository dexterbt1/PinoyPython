from django.db import models

class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField('publish_date')
    content = models.TextField()
    
class Category(models.Model):
    category_name = models.CharField(max_length=150)

class Tag(models.Model):
    tag_name = models.CharField(max_length=150)
    
class Author(models.Model):
    name = models.CharField(max_length=200)