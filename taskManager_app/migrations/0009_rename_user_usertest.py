# Generated by Django 3.2.7 on 2021-09-27 11:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('taskManager_app', '0008_rename_userfront_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserTest',
        ),
    ]
