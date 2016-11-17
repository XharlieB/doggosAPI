from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Doggo, Size, Raze
from .serializer import DoggosSerializer, UserSerializer, SizeSerializer, RazeSerializer
from django.contrib.auth.models import User

# Create your views here.
class SizeViewSet(ModelViewSet):
	queryset = Size.objects.all()
	serializer_class = SizeSerializer

class RazeViewSet(ModelViewSet):
	queryset = Raze.objects.all()
	serializer_class = RazeSerializer	

class DoggoViewSet(ModelViewSet):
	queryset = Doggo.objects.all()
	serializer_class = DoggosSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer