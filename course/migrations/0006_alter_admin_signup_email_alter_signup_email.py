# Generated by Django 5.1.7 on 2025-03-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_admin_signup_username_alter_signup_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_signup',
            name='email',
            field=models.EmailField(db_collation='utf8_bin', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(db_collation='utf8_bin', max_length=254, unique=True),
        ),
    ]
