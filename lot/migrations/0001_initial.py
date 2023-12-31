# Generated by Django 4.2.4 on 2023-08-23 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название лота')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('rating', models.IntegerField(null=True, verbose_name='Рейтинг')),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LotImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('lot_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lot.lot', verbose_name='Лот')),
            ],
        ),
    ]
