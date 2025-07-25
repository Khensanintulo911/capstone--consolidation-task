"""
This module handles user authentication.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(View):
    """Handles user login using Django's auth system."""
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = AuthenticationForm()
        return render(request, 'authentication/login.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
        messages.error(request, 'Invalid username or password.')
        return render(request, 'authentication/login.html', {'form': form})


class LogoutView(LoginRequiredMixin, View):
    """Handles user logout."""
    
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('home')


class RegisterView(View):
    """Handles user registration."""
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = UserCreationForm()
        return render(request, 'authentication/register.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('dashboard')
        return render(request, 'authentication/register.html', {'form': form})
