# Generated by Django 3.0.7 on 2021-09-19 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210918_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email_id',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
