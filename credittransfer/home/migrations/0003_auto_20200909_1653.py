# Generated by Django 3.0.8 on 2020-09-09 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200909_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='current_credit',
            new_name='credit',
        ),
    ]
