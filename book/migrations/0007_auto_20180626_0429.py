# Generated by Django 2.0.3 on 2018-06-26 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20180626_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('ADVENTURE', 'Aventura'), ('DRAMA', 'Drama'), ('FANTASY', 'Fantasía'), ('FICTION', 'Ficción'), ('ROMANCE', 'Romance'), ('HISTORY', 'Historia'), ('POETRY', 'Poesía')], max_length=20),
        ),
    ]
