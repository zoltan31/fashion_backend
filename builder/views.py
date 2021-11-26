# Create your views here.

from builder.models import User, Cloth
from builder.serializers import UserSerializer, ClothSerializer
from rest_framework import generics

#Generic views for User class:
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#Generic views for Plan class:
class ClothList(generics.ListCreateAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer


class ClothDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer
