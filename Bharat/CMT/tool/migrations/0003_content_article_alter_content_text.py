# Generated by Django 4.1.3 on 2023-07-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0002_content_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='Article',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='content',
            name='Text',
            field=models.CharField(default='', max_length=20000),
        ),
    ]
