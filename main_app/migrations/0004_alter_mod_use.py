# Generated by Django 4.1.3 on 2022-11-16 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_mod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod',
            name='use',
            field=models.CharField(choices=[('P', 'Performance'), ('A', 'Aesthetic'), ('S', 'Saftey'), ('PA', 'Performance & Aesthetic'), ('PS', 'Performance & Saftey'), ('SA', 'Saftey & Aesthetic'), ('A', 'All')], default='P', max_length=2),
        ),
    ]
