# Generated by Django 4.2.7 on 2024-11-06 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_cart_id_cart_card_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='card_id',
            new_name='cart_id',
        ),
    ]
