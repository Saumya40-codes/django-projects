# Generated by Django 4.1.7 on 2023-04-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_userlogin_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='email',
            field=models.EmailField(default='', max_length=200, unique=True),
        ),
    ]
