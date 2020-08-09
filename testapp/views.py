from django.shortcuts import render
from testapp.forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.views import APIView
from testapp.models import TodoList
from testapp.serializers import TodoListSerializer
from rest_framework.response import Response
# Create your views here.

def register_new_user(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form,
    }
    if form.is_valid():
        # print(form.cleaned_data)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username, email, password)

    return render(request, 'testapp/register.html', context = context)

def home_page_view(request):
    return HttpResponse('This is home page')


class TodoListView(APIView):
    def get(self, request, format =None):
        qs = TodoList.objects.all()
        eserializer = TodoListSerializer(qs, many = True)
        # print(type(eserializer))
        # eserializer = {'a':'b'}
        return Response(eserializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TodoListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status = 400)

class TodoListDetailView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            qs = TodoList.objects.get(id = id)
            serializer = TodoListSerializer(qs)
            return Response(serializer.data)
        except TodoList.DoesNotExist:
            pdata = {'msg':'Requested data is not present.'}
            return Response(pdata, status = 400)

    def put(self, request, id, *args, **kwargs):
        todolist = TodoList.objects.get(id = id)
        serializer = TodoListSerializer(todolist, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)

    def delete(self, request, id, *args, **kwargs):
        try:
            qs = TodoList.objects.get(id = id)
            qs.delete()
            pdata = {'msg':'Deleted Successfully'}
            return Response(pdata)
        except TodoList.DoesNotExist:
            pdata = {'msg':'Requested data is not present'}
            return Response(pdata, status = 400)




