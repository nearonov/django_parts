# Generated by Django 3.2.13 on 2024-05-04 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manufacturers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=256)),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacturers.manufacturer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
