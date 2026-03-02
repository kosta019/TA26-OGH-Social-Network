from django.urls import path
from .views import UserListView

app_name = 'login'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
]