from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Doggo, Raze, Size
from django.contrib.auth.models import User

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class DoggosSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Doggo
		fields = ('name','age','image','raze','user')

class RazeSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Raze
		fields = ('nameRaze','size')

class SizeSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Size
		fields = ('name')