# Generated by Django 4.2.11 on 2025-04-29 11:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0010_book_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='overview',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
