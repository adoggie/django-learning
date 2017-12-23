#coding:utf-8


permission_required(perm, login_url=None, raise_exception=False)

from django.contrib.auth.decorators import permission_required
@permission_required('polls.can_vote')
def my_view(request):


#PermissionRequiredMixin

	from django.contrib.auth.mixins import PermissionRequiredMixin

	class MyView(PermissionRequiredMixin, View):
	    permission_required = 'polls.can_vote'
	    # Or multiple of permissions:
	    permission_required = ('polls.can_open', 'polls.can_edit')

#AccessMixin
