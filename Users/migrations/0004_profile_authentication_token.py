# Generated by Django 3.0.7 on 2021-03-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20210314_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='authentication_Token',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]