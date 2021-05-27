# Generated by Django 3.1.6 on 2021-05-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210527_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='email',
            field=models.EmailField(default=1, max_length=32, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]