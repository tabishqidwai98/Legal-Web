# Generated by Django 3.1.6 on 2021-05-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0014_auto_20210511_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='Category',
            field=models.CharField(choices=[('a', 'Criminal Case'), ('b', 'Civil Case'), ('c', 'Marriage Dissolution'), ('d', 'Paternity and Child Custody'), ('e', 'Protection Orders Aganist Domestic Violence'), ('f', 'Name Changes'), ('g', 'Guardianship'), ('h', 'Termination of Parental Rights and Adoptions'), ('i', 'Juvenile Matters'), ('j', 'Emancipation and Approval of Underage Marriages.')], default='Criminal Case', max_length=10),
        ),
    ]
