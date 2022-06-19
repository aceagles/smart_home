# Generated by Django 4.0.5 on 2022-06-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmartSwitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_url', models.URLField()),
                ('toggle_url', models.URLField()),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]