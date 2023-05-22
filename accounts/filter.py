import django_filters
from django_filters import CharFilter

from .models import *


#FOR DASHBOARD SEARCH
class AnimeFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    genre = CharFilter(field_name='genre', lookup_expr='icontains')
    date_aired = CharFilter(field_name='date_aired', lookup_expr='icontains')

    class Meta:
        model = AnimeInfo
        fields = '__all__'
        exclude = ['image', 'description', 'reviews', 'season', 'status', 'rating']


#FOR HOME SEARCH
class AnimeInfoFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    genre = CharFilter(field_name='genre', lookup_expr='icontains')

    class Meta:
        model = AnimeInfo
        fields = ['name', 'genre', 'status', 'rating']
