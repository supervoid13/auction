# Generated by Django 4.2.4 on 2023-09-05 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lot', '0002_lotsection_alter_lotimages_image_lot_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]