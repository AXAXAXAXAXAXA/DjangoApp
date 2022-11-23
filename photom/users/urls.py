from django.urls import path, include

from users.views import Register
from users.views import Login

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('loginn/', Login.as_view(), name='login'),

    path('register/', Register.as_view(), name='register'),
]