# Generated by Django 5.0.2 on 2024-03-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_driving'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tvswarranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=12)),
                ('date', models.DateField()),
            ],
        ),
    ]
