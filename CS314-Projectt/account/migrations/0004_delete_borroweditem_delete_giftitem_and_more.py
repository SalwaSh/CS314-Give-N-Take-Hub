# Generated by Django 4.2.1 on 2023-05-25 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_borroweditem_giftitem_swapeditem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='borrowedItem',
        ),
        migrations.DeleteModel(
            name='giftItem',
        ),
        migrations.DeleteModel(
            name='swapedItem',
        ),
    ]
