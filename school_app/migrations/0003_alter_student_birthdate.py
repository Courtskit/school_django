# Generated by Django 4.0.3 on 2022-03-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0002_student_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]