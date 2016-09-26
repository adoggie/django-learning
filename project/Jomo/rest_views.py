from django.utils.crypto import get_random_string
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from Jomo.models import Test

class SerializerSimple(Serializer):
	pass

class TestView( GenericAPIView ):
	# renderer_classes = (JSONRenderer,)

	def get_queryset(self):
		data = []
		for _ in range(100):
			data.append({'index': _ + 1, 'name': get_random_string(20)})
		return data


	def get(self,request):
		data =[]
		for _ in range(100):
			data.append( {'index': _+1 ,'name': get_random_string(20) } )
		# data = User.objects.all()
		return Response(data)


class SerializerUser(ModelSerializer):

	class Meta:
		model = Test
		# fields = '__all__'
		fields = ('name','length')

	def to_representation(self, instance):
		# print self.data
		# print self.validated_data
		return {
			'name':instance.name,
			'len':instance.length
		}

class TestUserView(ListAPIView):
	queryset = Test.objects
	serializer_class =  SerializerUser
