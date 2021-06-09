import django_filters
from  django_filters import DateFilter,CharFilter
from .models import images

class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title',lookup_expr='icontains')
    content = CharFilter(field_name='content',lookup_expr='icontains')

    class Meta:
        model =images
        fields = ['title','content']

        
