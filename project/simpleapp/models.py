from django.db import models
from django.core.validators import MinValueValidator


class Post(models.Model):
    title = models.CharField(default='news', max_length=255)
    date_and_time = models.DateTimeField(auto_now_add=True)
    category_post = models.ManyToManyField('category', through='PostCategory')
    heading = models.CharField(max_length=32, default='Heading')
    text = models.TextField(max_length=1024, default='Your text...')
    rating_of_post = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


# Создаём модель товара
class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,  # названия товаров не должны повторяться
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',  # все продукты в категории будут доступны через поле products
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


#  создаём категорию, к которой будет привязываться товар
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться

    def __str__(self):
        return f'{self.name.title()}'