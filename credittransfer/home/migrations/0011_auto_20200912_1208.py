# Generated by Django 3.0.8 on 2020-09-12 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200912_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(auto_created=True, unique=True),
        ),
    ]
