# Generated by Django 2.0.7 on 2020-04-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0010_auto_20200404_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='uage',
            field=models.CharField(default='', max_length=10, verbose_name='年龄'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='upersonInf',
            field=models.CharField(default='', max_length=200, verbose_name='个人简介'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='usex',
            field=models.CharField(default='', max_length=10, verbose_name='性别'),
        ),
    ]
