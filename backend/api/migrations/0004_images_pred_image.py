# Generated by Django 5.0.4 on 2024-04-06 22:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_alter_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="images",
            name="pred_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="predicted_images/"
            ),
        ),
    ]
