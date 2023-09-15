
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('All-Userlist/', AllUserDetailsView.as_view(), name='my-profile'),
    path('list-filter/',UserlistDetailsView.as_view(),name='list-filter'),
    path('users/', UserListView.as_view(), name='user-list'),
]