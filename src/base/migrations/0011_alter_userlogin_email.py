# Generated by Django 4.1.7 on 2023-04-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_userlogin_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
