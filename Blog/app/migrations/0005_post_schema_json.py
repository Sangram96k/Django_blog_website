# Generated by Django 5.0.6 on 2024-07-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='schema_json',
            field=models.TextField(blank=True, null=True),
        ),
    ]
