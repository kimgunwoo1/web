# Generated by Django 4.1.5 on 2023-02-01 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=100)),
                ('mytitle', models.CharField(max_length=500)),
                ('mycontent', models.CharField(max_length=2000)),
                ('mydate', models.DateTimeField()),
            ],
        ),
    ]
