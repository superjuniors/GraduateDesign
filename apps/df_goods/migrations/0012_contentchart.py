# Generated by Django 2.0.7 on 2020-04-04 21:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0011_auto_20200402_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.BooleanField(default=False)),
                ('ctitle', models.CharField(max_length=20, verbose_name='商品名称')),
                ('cusername', models.CharField(max_length=20, verbose_name='评论者昵称')),
                ('cusername1', models.CharField(max_length=20, verbose_name='回复者昵称')),
                ('ccontent_chart', tinymce.models.HTMLField(max_length=200, verbose_name='评论回复')),
                ('date_publish', models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间')),
                ('cgoodsname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsContent', verbose_name='评论id')),
            ],
            options={
                'verbose_name': '评论回复',
                'verbose_name_plural': '评论回复',
            },
        ),
    ]