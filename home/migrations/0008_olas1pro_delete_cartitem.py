# Generated by Django 5.0.2 on 2024-03-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Olas1pro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=112)),
                ('address', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
