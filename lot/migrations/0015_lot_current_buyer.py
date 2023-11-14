# Generated by Django 4.2.4 on 2023-10-07 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lot', '0014_lot_highest_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='current_buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='competition_lots', to=settings.AUTH_USER_MODEL),
        ),
    ]
