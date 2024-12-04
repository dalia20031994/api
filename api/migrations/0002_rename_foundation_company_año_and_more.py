# Generated by Django 5.1.3 on 2024-12-04 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='foundation',
            new_name='año',
        ),
        migrations.RenameField(
            model_name='pelicula',
            old_name='website',
            new_name='imagen',
        ),
        migrations.RenameField(
            model_name='pelicula',
            old_name='name',
            new_name='titulo',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='descripcion',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
