# Generated by Django 4.0.4 on 2022-05-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
    ]