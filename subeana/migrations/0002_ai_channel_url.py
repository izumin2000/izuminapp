# Generated by Django 4.0.2 on 2022-06-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subeana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrics', models.CharField(default='', max_length=50)),
                ('isgood', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='url',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
