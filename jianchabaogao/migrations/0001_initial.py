# Generated by Django 3.1.5 on 2021-03-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jianchabaogao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frontdata1', models.CharField(max_length=100)),
                ('frontdata2', models.CharField(max_length=100)),
                ('frontdata3', models.CharField(max_length=100)),
                ('frontdata4', models.CharField(max_length=50)),
                ('frontdata5', models.CharField(max_length=50)),
                ('frontdata6', models.CharField(max_length=100)),
                ('frontdata7', models.CharField(max_length=100)),
                ('frontdata8', models.CharField(max_length=1000)),
            ],
        ),
    ]
