# Generated by Django 3.1.4 on 2020-12-10 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageURL',
            field=models.TextField(null=True),
        ),
    ]
