# Generated by Django 4.1 on 2023-11-08 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_note_delete_notes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='note',
        ),
    ]
