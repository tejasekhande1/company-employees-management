# Generated by Django 4.2.17 on 2025-01-05 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=10, unique=True)),
                ('position', models.CharField(max_length=100)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.company')),
            ],
        ),
    ]
