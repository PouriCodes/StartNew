# Generated by Django 4.2.20 on 2025-05-03 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_name_alter_comment_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='subject',
            new_name='subjects',
        ),
    ]
