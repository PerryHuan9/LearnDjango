# Generated by Django 2.1.2 on 2018-10-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
