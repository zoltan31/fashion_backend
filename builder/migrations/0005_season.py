# Generated by Django 3.2.9 on 2021-11-27 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0004_alter_cloth_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('active', models.BooleanField()),
            ],
        ),
    ]
