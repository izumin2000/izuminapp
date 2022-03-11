# Generated by Django 4.0.2 on 2022-03-11 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firstview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(default='', max_length=20)),
                ('player', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('uuid', models.CharField(default='', max_length=50)),
                ('info', models.CharField(default='', max_length=200)),
                ('rank', models.CharField(default='国民', max_length=20)),
                ('online', models.BooleanField(default=False)),
                ('primary', models.BooleanField(default=False)),
                ('leave', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Siteinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('visit', models.IntegerField(default=0)),
                ('nations', models.CharField(default='', max_length=10000)),
            ],
        ),
    ]
