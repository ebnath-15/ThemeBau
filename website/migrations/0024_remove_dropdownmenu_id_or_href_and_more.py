# Generated by Django 4.2 on 2023-08-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_submenu_file_path_dropdownmenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dropdownmenu',
            name='id_or_href',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='id_or_href',
        ),
        migrations.RemoveField(
            model_name='submenu',
            name='id_or_href',
        ),
        migrations.AddField(
            model_name='menu',
            name='file_path',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
