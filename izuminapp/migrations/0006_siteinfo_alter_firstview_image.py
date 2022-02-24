# Generated by Django 4.0.2 on 2022-02-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izuminapp', '0005_remove_firstview_display_remove_firstview_images_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siteinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('visit', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='firstview',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
