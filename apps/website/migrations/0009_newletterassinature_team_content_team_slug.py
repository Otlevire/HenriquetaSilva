# Generated by Django 4.2.7 on 2023-12-10 07:29

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_carrocel_local_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewletterAssinature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
