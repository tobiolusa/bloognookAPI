from django.urls import path
from .views import register_user, user_login, user_logout, total_users

urlpatterns = [
    path('register', register_user, name='register'),
    path('login', user_login, name="login"),
    path('logout', user_logout, name="logout"),
    path('total-users', total_users, name="total-users"),
]