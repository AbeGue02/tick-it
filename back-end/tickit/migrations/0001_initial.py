# Generated by Django 5.0.3 on 2024-03-25 22:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='no state name', max_length=100)),
                ('city', models.CharField(default='no city name', max_length=100)),
                ('city_img', models.TextField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no venue name', max_length=100)),
                ('venue_img', models.TextField(default='', max_length=300)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venue', to='tickit.location')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no event name', max_length=100)),
                ('event_type', models.CharField(default='no event type', max_length=100)),
                ('date', models.DateTimeField()),
                ('seating_type', models.CharField(default='no seating type', max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('event_img', models.TextField(default='', max_length=300)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='tickit.venue')),
            ],
        ),
    ]
