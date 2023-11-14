from django.urls import path
from users import views


urlpatterns = [
    path(r'login/', views.MyLoginView.as_view(), name='login'),
    path(r'logout/', views.MyLogoutView.as_view(), name='logout'),
    path(r'register/', views.RegisterView.as_view(), name='register'),
    path(r'profile/', views.user_profile_view, name='profile'),
    path(r'profile/top_up', views.top_up_balance, name='top_up_balance'),
    path(r'profile/edit', views.EditProfileView.as_view(), name='edit_profile'),
]
