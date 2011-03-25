# -*- coding: utf-8 -*-

from django.db import models

class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField('publish_date')
    content = models.TextField()

    class Meta:
        verbose_name = u"Blog Entry"
        verbose_name_plural = u"Blog Entries"

    
class Category(models.Model):
    category_name = models.CharField(max_length=150)

    class Meta:
        verbose_name = u"Category"
        verbose_name_plural = u"Categories"


class Tag(models.Model):
    tag_name = models.CharField(max_length=150)

    
class Author(models.Model):
    name = models.CharField(max_length=200)
