import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='iexact') 
    priority = django_filters.CharFilter(lookup_expr='iexact')
    due_date = django_filters.DateFilter()

    class Meta:
        model = Task
        fields = ['status', 'priority', 'due_date']
