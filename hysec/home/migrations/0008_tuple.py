# Generated by Django 4.1 on 2023-11-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_lectures_delete_lecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='tuple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayofweek', models.PositiveSmallIntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
            ],
        ),
    ]
