# Generated by Django 2.0 on 2021-05-20 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applyjob',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='joblisting',
            options={'ordering': ['-id']},
        ),
    ]
