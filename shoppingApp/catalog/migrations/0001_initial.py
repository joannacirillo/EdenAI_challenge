# Generated by Django 3.2.10 on 2021-12-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Product Name')),
                ('price', models.FloatField()),
                ('promotion', models.BooleanField()),
            ],
        ),
    ]