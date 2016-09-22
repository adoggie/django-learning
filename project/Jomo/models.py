from __future__ import unicode_literals

from django.db import models

# Create your models here.


class PigcmsUserinfo(models.Model):
    # id = models.TextField(primary_key=True)  # This field type is a guess.
    portrait = models.CharField(max_length=200)
    wallopen = models.TextField()  # This field type is a guess.
    total_score = models.TextField()  # This field type is a guess.
    expensetotal = models.TextField()  # This field type is a guess.
    token = models.CharField(max_length=60)
    wecha_id = models.CharField(max_length=60)
    wechaname = models.CharField(max_length=60)
    truename = models.CharField(max_length=60)
    tel = models.CharField(max_length=11)
    bornyear = models.CharField(max_length=4)
    bornmonth = models.CharField(max_length=4)
    bornday = models.CharField(max_length=4)
    qq = models.CharField(max_length=11)
    sex = models.TextField()  # This field type is a guess.
    age = models.CharField(max_length=3)
    birthday = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    info = models.CharField(max_length=200)
    sign_score = models.TextField()  # This field type is a guess.
    expend_score = models.TextField()  # This field type is a guess.
    continuous = models.TextField()  # This field type is a guess.
    add_expend = models.TextField()  # This field type is a guess.
    add_expend_time = models.TextField()  # This field type is a guess.
    live_time = models.TextField()  # This field type is a guess.
    getcardtime = models.TextField()  # This field type is a guess.
    balance = models.TextField()  # This field type is a guess.
    paypass = models.CharField(max_length=32, blank=True, null=True)
    twid = models.CharField(max_length=20)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    city = models.CharField(max_length=40, blank=True, null=True)
    province = models.CharField(max_length=40, blank=True, null=True)
    store_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    drp_cart = models.TextField()
    regtime = models.CharField(max_length=20)
    fakeopenid = models.CharField(max_length=100)
    issub = models.TextField()  # This field type is a guess.
    origin = models.CharField(max_length=200, blank=True, null=True)
    isverify = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pigcms_userinfo'
