# Generated by Django 4.1 on 2023-11-11 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0023_delete_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('education', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('limitcourse', models.CharField(max_length=50, null=True)),
                ('photo', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
