# Generated by Django 3.1.6 on 2021-05-31 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210531_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyer',
            name='city',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='contact',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='designation',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='experience',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='lawyertype',
            field=models.CharField(default='', max_length=25),
        ),
    ]