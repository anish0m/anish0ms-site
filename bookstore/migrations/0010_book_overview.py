# Generated by Django 4.2.11 on 2025-04-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0009_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='overview',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
