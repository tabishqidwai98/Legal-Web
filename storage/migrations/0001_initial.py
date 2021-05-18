# Generated by Django 3.1.6 on 2021-05-17 16:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseName', models.CharField(default='Case', max_length=255)),
                ('Category', models.CharField(choices=[('Criminal Case', 'Criminal Case'), ('Civil Case', 'Civil Case'), ('Marriage Dissolution', 'Marriage Dissolution'), ('Paternity and Child Custody', 'Paternity and Child Custody'), ('Protection Orders Aganist Domestic Violence', 'Protection Orders Aganist Domestic Violence'), ('Name Changes', 'Name Changes'), ('Guardianship', 'Guardianship'), ('Termination of Parental Rights and Adoptions', 'Termination of Parental Rights and Adoptions'), ('Juvenile Matters', 'Juvenile Matters'), ('Emancipation and Approval of Underage Marriages', 'Emancipation and Approval of Underage Marriages')], default='Criminal Case', max_length=50)),
                ('Description', models.TextField()),
                ('Case_image', models.ImageField(null=True, upload_to='Case_dir/images')),
                ('Contact_No', models.IntegerField(default=911234567890, unique=True)),
                ('email', models.EmailField(default='example@host.com', max_length=255)),
                ('Requested_on', models.DateTimeField(auto_now=True)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user_profile')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='review title', max_length=225)),
                ('detail', models.TextField()),
                ('rating', models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
                ('Case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.cases')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.user_profile')),
            ],
        ),
    ]
