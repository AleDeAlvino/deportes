# Generated by Django 2.2.5 on 2020-06-10 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='plan',
            field=models.CharField(choices=[('SOF18', 'SOF18'), ('LAT18', 'LAT18'), ('TEL18', 'TEL18'), ('INF18', 'INF18'), ('INC18', 'INC18')], max_length=5),
        ),
    ]
