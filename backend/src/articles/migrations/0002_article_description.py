# Generated by Django 2.2.1 on 2019-05-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default='Description'),
        ),
    ]
