# Generated by Django 4.1.7 on 2023-03-12 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_alter_posts_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.TextField()),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.posts"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Comments",
            },
        ),
    ]