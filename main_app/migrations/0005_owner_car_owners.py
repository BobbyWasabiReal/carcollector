# Generated by Django 4.1.3 on 2022-11-17 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_mod_use'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('years_owned', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='owners',
            field=models.ManyToManyField(to='main_app.owner'),
        ),
    ]
