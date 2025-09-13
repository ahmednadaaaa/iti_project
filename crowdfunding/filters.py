# crowdfunding/filters.py
import django_filters
from .models import Project
from django.utils import timezone

class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title', 
        lookup_expr='icontains', 
        label=''
    )
    
    category = django_filters.NumberFilter(
        field_name='category__id',
        label='Category'
    )
    
    status = django_filters.ChoiceFilter(
        choices=[('active', 'Active'), ('completed', 'Completed'), ('upcoming', 'Upcoming')],
        method='filter_by_status',
        label='Status'
    )
    
    sort = django_filters.ChoiceFilter(
        choices=[
            ('newest', 'Newest'),
            ('oldest', 'Oldest'),
            ('most_funded', 'Most Funded'),
            ('least_funded', 'Least Funded')
        ],
        method='filter_by_sort',
        label='Sort By'
    )
    
    class Meta:
        model = Project
        fields = ['title', 'category', 'status', 'sort']
    
    def filter_by_status(self, queryset, name, value):
        now = timezone.now()
        
        if value == 'active':
            return queryset.filter(start_time__lte=now, end_time__gte=now, is_canceled=False)
        elif value == 'completed':
            return queryset.filter(end_time__lt=now, is_canceled=False)
        elif value == 'upcoming':
            return queryset.filter(start_time__gt=now, is_canceled=False)
        return queryset
    
    def filter_by_sort(self, queryset, name, value):
        if value == 'newest':
            return queryset.order_by('-created_at')
        elif value == 'oldest':
            return queryset.order_by('created_at')
        elif value == 'most_funded':
            return queryset.order_by('-total_donations')
        elif value == 'least_funded':
            return queryset.order_by('total_donations')
        return queryset