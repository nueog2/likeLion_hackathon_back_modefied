# Generated by Django 3.2 on 2023-08-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewKiosk', '0002_auto_20230807_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
