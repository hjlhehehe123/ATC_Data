# Generated by Django 3.0.4 on 2020-05-31 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainningcompletion', '0002_monthplan_trainningstatusdetailother'),
    ]

    operations = [
        migrations.CreateModel(
            name='banzu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bzname', models.CharField(max_length=300)),
                ('bzperson', models.CharField(max_length=300)),
            ],
        ),
    ]