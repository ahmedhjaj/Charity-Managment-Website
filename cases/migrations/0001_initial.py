# Generated by Django 4.0.10 on 2023-05-13 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addDate', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('ML', 'Male'), ('FE', 'Female')], max_length=2)),
                ('job', models.CharField(max_length=150)),
                ('region', models.CharField(choices=[('BJ', 'Borj Al Arab'), ('AX', 'Alexandria')], max_length=2)),
                ('marriageStatus', models.CharField(choices=[('MA', 'Married'), ('SN', 'Signle'), ('WO', 'Widowed')], max_length=2)),
                ('birthDate', models.DateField()),
                ('nationalID', models.CharField(max_length=14)),
                ('nationalIDExpiration', models.DateField()),
                ('qualification', models.CharField(choices=[('HS', 'High School'), ('BA', 'Bachelor')], max_length=2)),
                ('phoneNumber', models.CharField(max_length=150)),
                ('gaurdianName', models.CharField(max_length=255)),
                ('gaurdianRelation', models.CharField(choices=[('BR', 'Brother'), ('SI', 'Sister'), ('MA', 'Mother'), ('OT', 'Other')], max_length=2)),
                ('gaudrianNumber', models.CharField(max_length=150)),
                ('housing', models.CharField(max_length=255)),
                ('caseDescribtion', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humanNeeds', models.CharField(max_length=300)),
                ('otherHelp', models.CharField(max_length=300)),
                ('interviewDescription', models.CharField(max_length=300)),
                ('interviewResult', models.CharField(max_length=300)),
                ('researcherOpinion', models.CharField(max_length=300)),
                ('supervisorOpinion', models.CharField(max_length=300)),
                ('overallRating', models.CharField(max_length=300)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='cases.case')),
            ],
        ),
        migrations.CreateModel(
            name='Medical_Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=255)),
                ('diseaseType', models.CharField(choices=[('ML', 'Male'), ('FE', 'Female')], max_length=2)),
                ('medicine', models.CharField(max_length=150)),
                ('insuranceID', models.IntegerField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_expenses', to='cases.case')),
            ],
        ),
        migrations.CreateModel(
            name='Family_Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('ML', 'Male'), ('FE', 'Female')], max_length=2)),
                ('age', models.IntegerField()),
                ('qualification', models.CharField(choices=[('HS', 'High School'), ('BA', 'Bachelor')], max_length=2)),
                ('occubation', models.CharField(max_length=150)),
                ('notes', models.CharField(max_length=150)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_members', to='cases.case')),
            ],
        ),
        migrations.CreateModel(
            name='Family_Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=150)),
                ('amount', models.IntegerField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_income', to='cases.case')),
            ],
        ),
        migrations.CreateModel(
            name='Family_Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=150)),
                ('amount', models.IntegerField()),
                ('notes', models.CharField(max_length=150)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_expenses', to='cases.case')),
            ],
        ),
    ]
