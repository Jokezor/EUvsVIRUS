# Generated by Django 3.0.5 on 2020-04-22 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_2', '0002_auto_20200422_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_2.City'),
        ),
    ]