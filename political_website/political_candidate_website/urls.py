"""
Main URL configuration for the political candidate website.

This module defines the URL patterns for the entire Django project,
including routes for candidate profiles, user authentication, contact forms,
and administrative functions.

URL Patterns:
    - Admin interface: /admin/
    - Home and welcome pages: / and /welcome/
    - Candidate functionality: /profile/, /login/, /logout/
    - User authentication: /register/ and Django's built-in auth URLs
    - Contact form: /contact/
"""

# Project:  political_candidate_website/urls.py
from django.contrib import admin
from django.urls import path, include
from candidate.views import profile, login_view, logout_view
from user_auth import views as auth_views
from django.views.generic import TemplateView
from contact.views import send_feedback

urlpatterns = [
    # Administrative interface
    path('admin/', admin.site.urls),

    # Public pages - handles the root path and welcome page
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('welcome/', TemplateView.as_view(template_name='welcome.html'), name='welcome'),

    # Candidate-specific URLs for profile and authentication
    path('profile/', profile, name='candidate_profile'),
    path('login/', login_view, name='candidate-login'),
    path('logout/', logout_view, name='candidate-logout'),

    # Django's built-in authentication URLs (password reset, etc.)
    # Includes: login/, logout/, password_change/, password_reset/, etc.
    path('', include('django.contrib.auth.urls')),

    # User registration endpoint
    path('register/', auth_views.register, name='register'),

    # Contact form for user feedback and inquiries
    path('contact/', send_feedback, name='contact'),
]

