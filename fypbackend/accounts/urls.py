from knox import views as knox_views
from .views import LoginAPI, RegisterAPI, UserAPI, ChangePasswordView, users_list, user_edit, user_delete
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/user/', UserAPI.as_view(), name='user'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/users/', users_list, name='users_list'),
    path('api/user_edit/', user_edit, name='user_edit'),
    path('api/user_delete/<int:id>/', user_delete, name='user_delete')
]