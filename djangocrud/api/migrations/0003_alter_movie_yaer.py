# Generated by Django 4.0.3 on 2022-04-02 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_movie_yaer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='yaer',
            field=models.CharField(max_length=32),
        ),
    ]
