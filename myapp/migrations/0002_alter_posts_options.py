# Generated by Django 4.1.7 on 2023-03-09 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="posts",
            options={"verbose_name_plural": "Posts"},
        ),
    ]