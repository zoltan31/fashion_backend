from django.urls import path
from django.utils import timezone
from builder import views
from builder.models import Season
from rest_framework.urlpatterns import format_suffix_patterns

from builder import admin

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('cloth/', views.ClothList.as_view()),
    path('cloth/<int:pk>/', views.ClothDetail.as_view()),
    path('clothes_required/', views.fv)
]
urlpatterns = format_suffix_patterns(urlpatterns)

style_list = ['retro', 'hypebeast', 'goth', 'smart-casual', 'alt', 'vintage', 'exotic', 'bohemian', 'sporty', 'military']


def check_season():
  seasons = Season.objects.all()
  for i in range(len(seasons)):
    season = seasons[i]
    if season.active:
      active_season = season
      active_season_index = i
      break
  
  isactive = timezone.make_naive(active_season.start_date) + timezone.timedelta(days=60) >= timezone.datetime.now()
  if not isactive:
    index = 0 if active_season_index + 1 >= len(seasons) else active_season_index + 1
    next_active_season = seasons[index]
    next_active_season.start_date = timezone.datetime.now()
    next_active_season.active = True
    active_season.active = False
    return next_active_season
  return active_season

# add_seasons()
check_season()