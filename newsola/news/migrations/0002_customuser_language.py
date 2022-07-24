# Generated by Django 4.0.4 on 2022-07-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='language',
            field=models.CharField(choices=[('English', 'en'), ('Russian', 'ru'), ('Deutsch', 'de'), ('Espagnol', 'es'), ('Français', 'fr'), ('Italiano', 'it')], default='1', max_length=20),
        ),
    ]
