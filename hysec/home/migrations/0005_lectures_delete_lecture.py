# Generated by Django 4.1 on 2023-11-07 05:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_lecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='lectures',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('lecturetitle', models.CharField(max_length=1000)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='lecture',
        ),
    ]
