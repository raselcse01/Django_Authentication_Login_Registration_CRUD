# Generated by Django 4.1.6 on 2023-03-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
