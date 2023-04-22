# Generated by Django 4.1.7 on 2023-04-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_userlogin_room_userlogin_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='email',
            field=models.EmailField(default='', help_text='Required. Inform a valid email address.', max_length=200, unique=True),
        ),
    ]