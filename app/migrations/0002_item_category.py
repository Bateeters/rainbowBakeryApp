# Generated by Django 3.2.14 on 2022-07-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]