# Generated by Django 3.0.3 on 2020-02-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=200)),
                ('isOn', models.BooleanField()),
                ('hour', models.CharField(max_length=2)),
                ('min', models.CharField(max_length=2)),
                ('repeat', models.BooleanField()),
                ('weekdays', models.CharField(max_length=27)),
            ],
        ),
    ]
