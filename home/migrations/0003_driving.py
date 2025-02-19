# Generated by Django 5.0.2 on 2024-03-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_maintenance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('model', models.CharField(max_length=122)),
                ('type', models.CharField(max_length=20)),
                ('pic', models.ImageField(upload_to='license_photos/')),
                ('date', models.DateField()),
            ],
        ),
    ]
