# Generated by Django 3.2.4 on 2021-06-22 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0004_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.CharField(blank=True, max_length=200, null=True)),
                ('time', models.CharField(blank=True, max_length=200, null=True)),
                ('post', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(blank=True, choices=[('New', 'New'), ('Read', 'Read')], max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
