# Generated by Django 3.0.7 on 2021-09-18 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='department',
            new_name='Highest_qualification',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll_no',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='phone_no',
        ),
    ]
