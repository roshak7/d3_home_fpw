from django.contrib import admin
from django.contrib import admin
from .models import Category, Product,Post,PostCategory

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Post)
admin.site.register(PostCategory)