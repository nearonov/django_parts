# Generated by Django 3.2.13 on 2024-05-13 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
    ]
