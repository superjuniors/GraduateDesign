# Generated by Django 2.0.7 on 2020-04-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_order', '0003_orderdetailinfo_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetailinfo',
            name='shopername',
            field=models.CharField(default='', max_length=20, verbose_name='卖家昵称'),
        ),
    ]
