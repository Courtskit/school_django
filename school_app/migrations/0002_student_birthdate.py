# Generated by Django 4.0.3 on 2022-03-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birthdate',
            field=models.DateField(default=None, null=True),
        ),
    ]