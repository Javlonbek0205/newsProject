# Generated by Django 5.0.6 on 2024-07-06 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_post',
            name='author',
            field=models.CharField(default='Anonim', max_length=30),
        ),
    ]