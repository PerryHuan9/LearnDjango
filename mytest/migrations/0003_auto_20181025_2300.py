# Generated by Django 2.1.2 on 2018-10-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0002_album_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
