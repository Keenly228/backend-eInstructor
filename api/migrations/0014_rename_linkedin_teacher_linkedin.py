# Generated by Django 4.2.7 on 2024-11-14 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_rename_prview_variantitem_preview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='Linkedin',
            new_name='linkedin',
        ),
    ]
