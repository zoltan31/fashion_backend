# Create your views here.

from builder.models import User, Cloth, Season
from builder.serializers import UserSerializer, ClothSerializer
from rest_framework import generics
from django.http import JsonResponse
from django.utils import timezone
import random
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

style_list = ['retro', 'hypebeast', 'goth', 'smart-casual', 'alt', 'vintage', 'exotic', 'bohemian', 'sporty', 'military']
type_list = ['socks', 't-shirt', 'hoodie', 'trousers', 'shirt', 'hat', 'pullover', 'footwear', 'accessory']
webshoplink = ['https://www2.hm.com/hu_hu/index.html', 'https://www.zara.com/hu/', 'https://www.aboutyou.hu', 'https://myspringfield.com/hu/hu']

def get_next_season():
  seasons = Season.objects.all()
  for i in range(len(seasons)):
    season = seasons[i]
    if season.active:
      active_season_index = i
      break
  index = 0 if active_season_index + 1 >= len(seasons) else active_season_index + 1
  return seasons[index]

def get_active_season():
  seasons = Season.objects.all()
  for i in range(len(seasons)):
    season = seasons[i]
    if season.active:
      return season


def fv(request):
    next_season = get_next_season()
    clothes = Cloth.objects.all()
    clothes = filter(lambda i: timezone.make_naive(i.date_of_purchase) + timezone.timedelta(days=60) >= timezone.datetime.now(), clothes)
    clothes = filter(lambda i: i.style == next_season.name, clothes)
    cloth_types = set([cloth.type for cloth in clothes])
    types_needed = set(type_list).difference(cloth_types)

    webshop_url = random.choice(webshoplink)
    active_season = get_active_season()

    response = {
      "types_needed": list(types_needed),
      "expired_clothes": list(clothes),
      "active_style": active_season.name,
      "current_season_start": timezone.make_naive(active_season.start_date) - timezone.timedelta(days=60),
      "next_season_start": next_season.start_date,
      "next_style": next_season.name,
      "webshop_url": webshop_url
    }
    return JsonResponse(response)
