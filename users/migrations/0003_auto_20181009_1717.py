# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_last_login_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.CharField(default=b'1997-10-31', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='graduate_time',
            field=models.CharField(default=b'2008-10-10', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='id_number',
            field=models.CharField(default=b'111111111111111', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(default=b'\xe5\xb7\xa5\xe7\xa8\x8b\xe5\xb8\x88', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='job_2',
            field=models.CharField(default=b'\xe5\x91\x98\xe5\xb7\xa5', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='job_join_time',
            field=models.CharField(default=b'2019-10-10', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='job_number',
            field=models.CharField(default=b'0001', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='job_time',
            field=models.CharField(default=b'2015-10-31', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=b'\xe7\xac\xac\xe4\xb8\x80\xe6\xac\xa1\xe7\x99\xbb\xe5\xbd\x95', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=b'1888888888', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.CharField(default=b'\xe5\x8c\x97\xe4\xba\xac\xe5\xa4\xa7\xe5\xad\xa6', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(default=b'\xe7\x94\xb7', max_length=3),
        ),
        migrations.AddField(
            model_name='user',
            name='team_belong',
            field=models.CharField(default=b'C640', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='xueli',
            field=models.CharField(default=b'\xe6\x9c\xac\xe7\xa7\x91', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='zhengzhi_mianmao',
            field=models.CharField(default=b'\xe7\xbe\xa4\xe4\xbc\x97', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='zhengzhi_time',
            field=models.CharField(default=b'2010-10-31', max_length=20),
        ),
    ]
