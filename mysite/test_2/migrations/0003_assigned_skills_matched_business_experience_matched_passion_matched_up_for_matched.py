# Generated by Django 3.0.5 on 2020-04-26 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_2', '0002_matched_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Up_For_Matched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=100)),
                ('colab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_2.Collaboration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Passion_Matched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=100)),
                ('colab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_2.Collaboration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business_Experience_Matched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=100)),
                ('colab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_2.Collaboration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assigned_Skills_Matched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=100)),
                ('colab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_2.Collaboration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
