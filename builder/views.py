# Create your views here.

from builder.models import User, Cloth
from builder.serializers import UserSerializer, ClothSerializer
from rest_framework import generics
from django.http import JsonResponse
from django.utils import timezone
import datetime as dt
active_style = 'retro'
next_style = 'goth'
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

def fv(request):
    style_list = ['retro', 'hypebeast', 'goth', 'smart-casual',
    'alt', 'vintage', 'exotic', 'bohemian', 'sporty', 'military']
    type_list = ['socks', 't-shirt', 'hoodie', 'trousers', 'shirt',
    'hat', 'pullover', 'footwear', 'accessory']
    
    ctr_next = 0
    expired_type = []
    clothes = Cloth.objects.all().copy()
    clothes = filter(lambda i: i.date_of_purchase+dt.timedelta(days=60)<= dt.datetime.now(), clothes)
    clothes = filter(lambda i: i.style == next_style, clothes)
    for i in clothes:
        if i.style == next_style:
            ctr_next+=1
            
    

"clohtes.objecs.all összes ruha, aztán végigiterálok rajta"
"return: JSON"
