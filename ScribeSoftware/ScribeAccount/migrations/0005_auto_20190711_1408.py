# Generated by Django 2.2.3 on 2019-07-11 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ScribeAccount', '0004_auto_20190711_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scribecredentials',
            old_name='user_profile',
            new_name='scribe_profile',
        ),
    ]