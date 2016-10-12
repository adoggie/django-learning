# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-06 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PigcmsUserinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portrait', models.CharField(max_length=200)),
                ('wallopen', models.TextField()),
                ('total_score', models.TextField()),
                ('expensetotal', models.TextField()),
                ('token', models.CharField(max_length=60)),
                ('wecha_id', models.CharField(max_length=60)),
                ('wechaname', models.CharField(max_length=60)),
                ('truename', models.CharField(max_length=60)),
                ('tel', models.CharField(max_length=11)),
                ('bornyear', models.CharField(max_length=4)),
                ('bornmonth', models.CharField(max_length=4)),
                ('bornday', models.CharField(max_length=4)),
                ('qq', models.CharField(max_length=11)),
                ('sex', models.TextField()),
                ('age', models.CharField(max_length=3)),
                ('birthday', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=200)),
                ('sign_score', models.TextField()),
                ('expend_score', models.TextField()),
                ('continuous', models.TextField()),
                ('add_expend', models.TextField()),
                ('add_expend_time', models.TextField()),
                ('live_time', models.TextField()),
                ('getcardtime', models.TextField()),
                ('balance', models.TextField()),
                ('paypass', models.CharField(blank=True, max_length=32, null=True)),
                ('twid', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('province', models.CharField(blank=True, max_length=40, null=True)),
                ('store_id', models.TextField(blank=True, null=True)),
                ('drp_cart', models.TextField()),
                ('regtime', models.CharField(max_length=20)),
                ('fakeopenid', models.CharField(max_length=100)),
                ('issub', models.TextField()),
                ('origin', models.CharField(blank=True, max_length=200, null=True)),
                ('isverify', models.TextField()),
            ],
            options={
                'db_table': 'pigcms_userinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('length', models.IntegerField()),
            ],
        ),
    ]