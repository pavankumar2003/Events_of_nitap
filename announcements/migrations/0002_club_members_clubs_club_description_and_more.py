# Generated by Django 4.0.3 on 2023-02-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='club_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.IntegerField()),
                ('stu_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='clubs',
            name='club_description',
            field=models.TextField(default='welcome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clubs',
            name='club_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
