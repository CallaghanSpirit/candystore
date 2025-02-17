from django.urls import path
from users  import views


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password-change-done/', views.UserPasswordChangeDone.as_view(), name='password_change_done'),
    
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile')
    


]
