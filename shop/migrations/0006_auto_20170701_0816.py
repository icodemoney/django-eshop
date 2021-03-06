# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-01 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_shopcart_appendtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='active',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to='active', verbose_name='\u5c01\u9762'),
        ),
        migrations.AlterField(
            model_name='active',
            name='name',
            field=models.CharField(max_length=64, verbose_name='\u6d3b\u52a8\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='cell',
            name='url',
            field=models.CharField(max_length=128, verbose_name='\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='mycoupon',
            name='useStatus',
            field=models.CharField(choices=[('KY', '\u53ef\u7528'), ('BKY', '\u4e0d\u53ef\u7528'), ('ZZSY', '\u6b63\u5728\u4f7f\u7528'), ('YGQ', '\u5df2\u8fc7\u671f'), ('YSY', '\u5df2\u4f7f\u7528')], default='KY', max_length=4, verbose_name='\u53ef\u7528\u72b6\u6001'),
        ),
    ]
