from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Task
from .serializers import TaskSerializer

class TaskFilter(filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'title': ['exact', 'icontains'], 
            'description': ['exact', 'icontains'], 
            'completed': ['exact'],            
            'created_at': ['exact', 'gte', 'lte'], 
        }

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter
