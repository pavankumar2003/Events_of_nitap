# Generated by Django 4.0.3 on 2023-04-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0013_events_club_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='events_pics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.CharField(max_length=6)),
                ('event_id', models.IntegerField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
    ]
