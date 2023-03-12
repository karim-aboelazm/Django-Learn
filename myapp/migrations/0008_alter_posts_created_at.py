# Generated by Django 4.1.7 on 2023-03-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0007_posts_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="created_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="post created at"
            ),
        ),
    ]