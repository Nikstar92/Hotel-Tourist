# Generated by Django 4.2 on 2023-04-26 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touristapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id'], 'verbose_name': 'Пользователя', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
