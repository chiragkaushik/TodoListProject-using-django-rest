from django.shortcuts import render
from testapp.forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponse
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
