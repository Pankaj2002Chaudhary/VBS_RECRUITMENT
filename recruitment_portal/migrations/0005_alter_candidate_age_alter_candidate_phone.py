# Generated by Django 5.1.1 on 2024-09-26 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment_portal', '0004_candidate_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='age',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
