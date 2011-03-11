from blog.models import BlogEntry, Category, Tag, Author
from django.contrib import admin

admin.site.register(BlogEntry)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)