# Generated by Django 3.0.7 on 2020-08-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shorturl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('short_query', models.CharField(max_length=8)),
                ('visits', models.IntegerField(default=0)),
            ],
        ),
    ]
