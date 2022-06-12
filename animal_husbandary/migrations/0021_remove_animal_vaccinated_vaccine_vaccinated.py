# Generated by Django 4.0 on 2022-02-05 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_husbandary', '0020_remove_vaccine_vaccinated_animal_vaccinated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='vaccinated',
        ),
        migrations.AddField(
            model_name='vaccine',
            name='vaccinated',
            field=models.ManyToManyField(to='animal_husbandary.animal'),
        ),
    ]
