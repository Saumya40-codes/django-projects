# Generated by Django 4.1.7 on 2023-04-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_userlogin_room_alter_userlogin_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='email',
            field=models.EmailField(default='', max_length=200, null=True, unique=True),
        ),
    ]