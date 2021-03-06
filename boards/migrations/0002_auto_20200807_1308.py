# Generated by Django 3.1 on 2020-08-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrazilData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('cases', models.PositiveIntegerField(default=0, verbose_name='cases')),
                ('deaths', models.PositiveIntegerField(default=0, verbose_name='deaths')),
            ],
        ),
        migrations.CreateModel(
            name='SaoPauloData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('cases', models.PositiveIntegerField(default=0, verbose_name='cases')),
                ('deaths', models.PositiveIntegerField(default=0, verbose_name='deaths')),
            ],
        ),
        migrations.CreateModel(
            name='SudesteData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('cases', models.PositiveIntegerField(default=0, verbose_name='cases')),
                ('deaths', models.PositiveIntegerField(default=0, verbose_name='deaths')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='board',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='starter',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
