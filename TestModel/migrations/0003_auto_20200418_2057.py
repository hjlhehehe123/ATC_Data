# Generated by Django 3.0.4 on 2020-04-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='logins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atcAccount', models.CharField(max_length=18)),
                ('atcPassword', models.CharField(max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
