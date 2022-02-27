# Generated by Django 4.0.2 on 2022-02-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izuminapp', '0008_delete_oldjson_player_leave_player_uuid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='rank',
            field=models.CharField(default='国民', max_length=20),
        ),
        migrations.AlterField(
            model_name='firstview',
            name='player',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='firstview',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='info',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='uuid',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='nations',
            field=models.CharField(default='', max_length=10000),
        ),
    ]