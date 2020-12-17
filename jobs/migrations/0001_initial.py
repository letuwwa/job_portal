# Generated by Django 2.0 on 2020-12-17 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=200)),
                ('employment_status', models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Freelance', 'Freelancer')], max_length=10)),
                ('vacancy', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Any', 'Any')], max_length=30, null=True)),
                ('category', models.CharField(choices=[('Web Design', 'Web Design'), ('Graphic Design', 'Graphic Design'), ('Web Developing', 'Web Developing'), ('Software Engineering', 'Software Engineering'), ('HR', 'HR'), ('Marketing', 'Marketing')], max_length=30)),
                ('description', models.TextField()),
                ('responsibilities', models.TextField()),
                ('experience', models.CharField(max_length=100)),
                ('job_location', models.CharField(max_length=120)),
                ('Salary', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('application_deadline', models.DateTimeField()),
                ('published_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
