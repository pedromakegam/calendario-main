# Generated by Django 5.0.4 on 2024-06-09 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_event_apoio_linha_viva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='postes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
