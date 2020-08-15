from rest_framework.serializers import ModelSerializer
from testapp.models import TodoList, TodoItem, Access
from rest_framework import serializers

class TodoItemSerializer(ModelSerializer):
    class Meta:
        model = TodoItem
        # fields = ['id', 'list_id', 'heading', 'scheduled_on', 'created_at', 'updated_at', 'is_active']
        fields = '__all__'


class TodoListSerializer(ModelSerializer):
    # list_id_interaction = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    # list_id = TodoItemSerializer(source = 'list_id', many = True, read_only = True)
    # list_id_interaction = TodoItemSerializer(many=True)
    class Meta:
        model = TodoList
        # fields = ['id', 'name', 'list_id_interaction']
        fields = '__all__'

    # def create(self, validated_data):
    #     list_id_data = validated_data.pop('list_id')
    #     todolist_id = TodoList.objects.create(**validated_data)
    #     TodoItem.objects.create(list_id=todolist_id, **list_id_data)
    #     return todolist_id

class AccessSerializer(ModelSerializer):
    class Meta:
        model = Access
        fields = "__all__"

