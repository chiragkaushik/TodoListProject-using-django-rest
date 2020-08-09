from rest_framework.serializers import ModelSerializer
from testapp.models import TodoList

class TodoListSerializer(ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
