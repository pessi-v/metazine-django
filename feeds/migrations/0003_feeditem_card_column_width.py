# Generated by Django 5.1.3 on 2024-11-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feeds", "0002_feeditem_og_description_feeditem_og_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="feeditem",
            name="card_column_width",
            field=models.IntegerField(default=2),
        ),
    ]
