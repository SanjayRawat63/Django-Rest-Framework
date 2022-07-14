# Generated by Django 4.0.6 on 2022-07-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_age', models.PositiveIntegerField()),
                ('emp_designation', models.CharField(max_length=100)),
            ],
        ),
    ]
