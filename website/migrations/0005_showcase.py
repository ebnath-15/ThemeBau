# Generated by Django 4.2 on 2023-08-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_websitesettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='showcase/')),
            ],
        ),
    ]
