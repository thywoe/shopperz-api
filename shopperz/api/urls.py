from django.urls import path
from .views import AllViews

urlpatterns = [
    path('users/', AllViews.as_view(), name='user-list')
]


