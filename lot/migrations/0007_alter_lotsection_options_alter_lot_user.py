# Generated by Django 4.2.4 on 2023-09-24 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lot', '0006_alter_lot_options_lot_user_alter_lot_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lotsection',
            options={'verbose_name': 'раздел', 'verbose_name_plural': 'разделы'},
        ),
        migrations.AlterField(
            model_name='lot',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
