# Generated by Django 4.0.10 on 2023-05-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='gaurdianRelation',
            field=models.CharField(choices=[('BR', 'Brother'), ('SI', 'Sister'), ('MA', 'Mother'), ('OT', 'Other')], max_length=2),
        ),
    ]