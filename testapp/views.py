from django.shortcuts import render
from testapp.forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.views import APIView
from testapp.models import TodoList, TodoItem, Access
from testapp.serializers import TodoListSerializer, TodoItemSerializer, AccessSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from testapp.permissions import MyCustomReadPermission, MyCustomWritePermission
from django.shortcuts import get_object_or_404
# Create your views here.

def register_new_user(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        # print(form.cleaned_data)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username, email, password)

    return render(request, 'testapp/register.html', context=context)


def home_page_view(request):
    return HttpResponse('This is home page')




class TodoListView(APIView):
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [MyCustomReadPermission, ]
    def get(self, request):
        qs = TodoList.objects.all()
        eserializer = TodoListSerializer(qs, many=True)
        return Response(eserializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

class TodoListDetailView(APIView):
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [MyCustomReadPermission, ]

    def _get_permissions(self, request):
        if request.method == 'PUT':
            permission_classes = [MyCustomWritePermission, ]
        # pass
    def get(self, request, id, *args, **kwargs):
        try:
            qs = TodoList.objects.get(id=id)
            print(type(qs))
            serializer = TodoListSerializer(qs)
            return Response(serializer.data)
        except TodoList.DoesNotExist:
            pdata = {'msg': 'Requested data is not present.'}
            return Response(pdata, status=400)

    def put(self, request, id, *args, **kwargs):
        self._get_permissions(request)
        todolist = TodoList.objects.get(id=id)
        serializer = TodoListSerializer(todolist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, *args, **kwargs):
        try:
            qs = TodoList.objects.get(id=id)
            qs.delete()
            pdata = {'msg': 'Deleted Successfully'}
            return Response(pdata)
        except TodoList.DoesNotExist:
            pdata = {'msg': 'Requested data is not present'}
            return Response(pdata, status=400)


class TodoItemView(APIView):
    def get(self, request):
        qs = TodoItem.objects.all()
        print(qs)
        serializer = TodoItemSerializer(qs, many=True)
        print(serializer.data)
        print(qs)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class TodoItemDetailView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            qs = TodoItem.objects.get(id=id)
            serializer = TodoItemSerializer(qs)
            return Response(serializer.data)
        except TodoItem.DoesNotExist:
            pdata = {'msg': 'Requested data is not present.'}
            return Response(pdata, status=400)

    def put(self, request, id, *args, **kwargs):
        todoitem = TodoItem.objects.get(id=id)
        serializer = TodoItemSerializer(todoitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, *args, **kwargs):
        try:
            todoitem = TodoItem.objects.get(id=id)
            todoitem.delete()
            pdata = {'msg': 'Deleted Successfully'}
            return Response(pdata)
        except TodoItem.DoesNotExist:
            pdata = {'msg': 'Requested data is not present'}
            return Response(pdata, status=400)


class AccessView(APIView):
    def get(self, request):
        qs = Access.objects.all()
        serializer = AccessSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class AccessDetailView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            access = Access.objects.get(id=id)
            serializer = AccessSerializer(access)
            return Response(serializer.data)
        except Access.DoesNotExist:
            pdata = {'msg': 'Data does not exist'}
            return Response(pdata, status=400)

    def put(self, request, id, *args, **kwargs):
        try:
            access = Access.objects.get(id=id)
        except Access.DoesNotExist:
            pdata = {'msg': 'Requested data is not present'}
            return Response(pdata, status=400)

        serializer = AccessSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, id, *args, **kwargs):
        try:
            access = Access.objects.get(id=id)
            access.delete()
            pdata = {'msg': 'Requested data deleted successfully.'}
            return Response(pdata)
        except Access.DoesNotExist:
            pdata = {'msg': 'Requested data is not present'}
            return Response(pdata, status=400)
