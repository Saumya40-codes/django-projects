# Generated by Django 4.2 on 2023-04-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_delete_userlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loginpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
