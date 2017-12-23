#coding:utf-8

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

 user = get_object_or_404(User, pk=user_id)
