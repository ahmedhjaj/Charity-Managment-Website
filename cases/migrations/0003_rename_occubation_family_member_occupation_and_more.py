# Generated by Django 4.0.10 on 2023-05-14 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_notes_noteheader'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family_member',
            old_name='occubation',
            new_name='occupation',
        ),
        migrations.AlterField(
            model_name='medical_expenses',
            name='diseaseType',
            field=models.CharField(max_length=255),
        ),
    ]
