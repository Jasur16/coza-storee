# Generated by Django 4.1.1 on 2022-09-27 07:10

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='full name')),
            ],
            options={
                'verbose_name': 'auther',
                'verbose_name_plural': 'authers',
            },
        ),
        migrations.CreateModel(
            name='PostTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='tag')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='body')),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='body')),
                ('body_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='body')),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='body')),
                ('image', models.ImageField(upload_to='posts', verbose_name='image')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='posts_2', verbose_name='image_2')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='posts', to='blogs.authermodel')),
                ('tag', models.ManyToManyField(related_name='posts', to='blogs.posttagmodel', verbose_name='tag')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comment')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.CharField(max_length=13, verbose_name='phone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.postmodel', verbose_name='post')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
