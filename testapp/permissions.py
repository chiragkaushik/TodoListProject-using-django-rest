from rest_framework.permissions import BasePermission, SAFE_METHODS
from testapp.models import Access, User, TodoList
from testapp.serializers import TodoListSerializer, AccessSerializer

class MyCustomReadPermission(BasePermission):
    # def has_permission(self, request, view):
        # username = request.user.username
        # user_id = User.objects.get(username = username).id
        # print(user_id)

        # return True

    def has_object_permission(self, request, view, obj):
        username = request.user.username
        user_id = User.objects.get(username=username)
        # list_id = obj.objects.get('id')
        serializer = TodoListSerializer(obj)
        list_id = serializer.data.get('id')

        permission = Access.objects.filter(user_id = user_id, list_id = list_id).exists()
        print(permission)
        if permission:
            return True
        else:
            return False 

class MyCustomWritePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        username = request.user.username
        user_id = User.objects.get(username=username)
        # list_id = obj.objects.get('id')
        serializer = TodoListSerializer(obj)
        list_id = serializer.data.get('id')

        permission = Access.objects.filter(user_id=user_id, list_id=list_id).exists()
        print(permission)
        if permission:
            permission_type = Access.objects.filter(user_id=user_id, list_id=list_id)
            serializer = AccessSerializer(permission_type)
            if serializer.get('permission_type') == 'write':
                return True
            else:
                return False
        else:
            return False




