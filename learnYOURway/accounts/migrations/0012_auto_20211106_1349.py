# Generated by Django 3.0.7 on 2021-11-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20211106_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email_id',
        ),
        migrations.AddField(
            model_name='user',
            name='email_id',
            field=models.EmailField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.IntegerField(choices=[(3, 'PENDING'), (1, 'SUCCESS'), (2, 'FAILURE')], default=3),
        ),
    ]