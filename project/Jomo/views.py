from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class RedisTestView(TemplateView):
	template_name = 'Jomo/test_redis.html'

	def get_context_data(self, **kwargs):
		ctx = super(RedisTestView,self).get_context_data(**kwargs)
		ctx['server_url'] ='redis://192.168.199.235:6379'

		# from devops.models import PigcmsUserinfo
		# ctx['userinfo_list'] = PigcmsUserinfo.objects.all()
		
		return ctx