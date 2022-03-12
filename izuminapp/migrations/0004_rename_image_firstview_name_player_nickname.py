# Generated by Django 4.0.2 on 2022-03-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izuminapp', '0003_alter_firstview_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firstview',
            old_name='image',
            new_name='name',
        ),
        migrations.AddField(
            model_name='player',
            name='nickname',
            field=models.CharField(default='', max_length=50),
        ),
    ]