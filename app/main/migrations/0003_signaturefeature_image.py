# Generated by Django 5.0 on 2023-12-07 22:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_signaturefeature"),
    ]

    operations = [
        migrations.AddField(
            model_name="signaturefeature",
            name="image",
            field=models.ImageField(default="", upload_to="signatures_feature/", verbose_name="изображение"),
            preserve_default=False,
        ),
    ]