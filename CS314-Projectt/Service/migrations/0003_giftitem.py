# Generated by Django 4.2.1 on 2023-05-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0002_swapeditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='giftItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
