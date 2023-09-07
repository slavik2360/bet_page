# Generated by Django 4.2.3 on 2023-09-05 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='баннер')),
                ('banner_file', models.ImageField(default='main/unknown.jpeg', upload_to='main', verbose_name='файл баннера')),
                ('is_active', models.BooleanField(default=False, verbose_name='активный')),
            ],
            options={
                'verbose_name': 'баннер',
                'verbose_name_plural': 'баннеры',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(choices=[('0', 'Колесо фартуны'), ('1', 'Игровой Автомат')], max_length=200, verbose_name='игра')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='сумма')),
                ('coef', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='коефицент')),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='кто поставил')),
            ],
            options={
                'verbose_name': 'Ставка',
                'verbose_name_plural': 'Ставки',
                'ordering': ('-id',),
            },
        ),
    ]
