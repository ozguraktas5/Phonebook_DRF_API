# Generated by Django 4.2.4 on 2023-08-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("phonebook_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="address",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="categories",
            field=models.ManyToManyField(
                related_name="contacts", to="phonebook_app.category"
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="uploads"),
        ),
    ]