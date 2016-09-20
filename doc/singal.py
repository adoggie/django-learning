#coding:utf-8

from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.core.mail import send_mail

class Document(models.Model):
    [...]

class Comment(models.Model):
    [...]

def notify_admin(sender, instance, created, **kwargs):
    '''Notify the administrator that a new user has been added.'''
    if created:
       subject = 'New user created'
       message = 'User %s was added' % instance.username
       from_addr = 'no-reply@example.com'
       recipient_list = ('admin@example.com',)
       send_mail(subject, message, from_addr, recipient_list)

signals.post_save.connect(notify_admin, sender=User)

# post_save signal 由 Django 提供，每次保存或创建模型时都会激活。connect() 方法带有两个参数：一个回调参数（notify_admin）和 sender 参数，后者指定该回调只关注 User 模型的保存事件。