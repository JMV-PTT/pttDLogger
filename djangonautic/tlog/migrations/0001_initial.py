# Generated by Django 2.0.7 on 2018-07-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idKey', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('temp', models.CharField(max_length=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]