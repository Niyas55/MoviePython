# Generated by Django 4.2.3 on 2023-07-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ddffss', upload_to=''),
            preserve_default=False,
        ),
    ]
