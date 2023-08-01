# Generated by Django 3.2.19 on 2023-07-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=150, verbose_name='Viloyat nomi: ')),
                ('lat', models.CharField(max_length=150, verbose_name='Viloyat kengligi: ')),
                ('lon', models.CharField(max_length=150, verbose_name='Viloyat uzunligi: ')),
                ('weather_status', models.TextField(verbose_name='Viloyat ob havosi icon: ')),
            ],
        ),
    ]