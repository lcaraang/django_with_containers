# Generated by Django 2.1.15 on 2022-06-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(default='', max_length=20)),
                ('last', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=20)),
            ],
        ),
    ]