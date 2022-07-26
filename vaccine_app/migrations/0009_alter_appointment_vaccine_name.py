# Generated by Django 4.0.3 on 2022-03-25 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine_app', '0008_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='vaccine_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='vaccine_app.vaccine'),
        ),
    ]
