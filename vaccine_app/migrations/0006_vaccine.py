# Generated by Django 4.0.3 on 2022-03-24 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine_app', '0005_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
