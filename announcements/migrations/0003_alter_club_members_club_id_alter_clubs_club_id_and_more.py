# Generated by Django 4.0.3 on 2023-02-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_club_members_clubs_club_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club_members',
            name='club_id',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='club_id',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='events',
            name='club_id',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(),
        ),
    ]
