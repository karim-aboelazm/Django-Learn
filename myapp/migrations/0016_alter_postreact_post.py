# Generated by Django 4.1.7 on 2023-03-13 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0015_alter_postreact_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postreact",
            name="post",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.posts"
            ),
        ),
    ]