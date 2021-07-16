# Generated by Django 3.2.4 on 2021-07-15 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_post', models.CharField(default='news', max_length=255)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(default='Heading', max_length=32)),
                ('text', models.TextField(default='Your text...', max_length=1024)),
                ('rating_of_post', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category_post',
            field=models.ManyToManyField(through='simpleapp.PostCategory', to='simpleapp.Category'),
        ),
    ]