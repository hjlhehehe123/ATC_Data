# Generated by Django 3.0.4 on 2020-05-31 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainningcompletion', '0004_auto_20200531_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainningstatusdetailother',
            name='frontdata13',
        ),
        migrations.RemoveField(
            model_name='trainningstatusdetailother',
            name='frontdata14',
        ),
    ]
