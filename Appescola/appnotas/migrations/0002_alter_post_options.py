# Generated by Django 3.2.8 on 2021-10-26 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appnotas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',)},
        ),
    ]
