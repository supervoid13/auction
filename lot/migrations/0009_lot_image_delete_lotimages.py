# Generated by Django 4.2.4 on 2023-10-02 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lot', '0008_alter_lot_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='image',
            field=models.ImageField(blank=True, upload_to='lots_images', verbose_name='Фото лота'),
        ),
        migrations.DeleteModel(
            name='LotImages',
        ),
    ]