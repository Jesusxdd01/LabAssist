# Generated by Django 5.1.3 on 2024-11-10 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='custom_user_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
