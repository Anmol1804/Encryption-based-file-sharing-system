# Generated by Django 3.0 on 2020-11-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_userdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='file_upload',
            field=models.TextField(),
        ),
    ]
