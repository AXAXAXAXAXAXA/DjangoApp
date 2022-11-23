from django.contrib.auth import login, authenticate
from django.forms import TextInput, CharField
from django.views import View
from django.shortcuts import render, redirect

from users.forms import UserCreationForm
from users.forms import LoginForm


class Register(View):
    template_name = 'registration/register.html'
    #
    # class Meta:
    #     widgets = {
    #         "username": TextInput(attrs={
    #             'claas': 'form-control'
    #         })
    #     }

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class Login(View):
    template_name = 'registration/login.html'

    def get(self, request):
        context = {
            'form1': LoginForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form1': form
        }
        return render(request, self.template_name, context)
