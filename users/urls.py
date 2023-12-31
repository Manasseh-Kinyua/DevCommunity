from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.profile, name='user-profile'),
    path('account/', views.userAccount, name='account'),
    path('edit-profile/', views.editProfile, name='edit-profile'),

    path('add-skill/', views.addSkill, name='add-skill'),
    path('edit-skill/<str:pk>/', views.editSkill, name='edit-skill'),
    path('delete-skill/<str:pk>/', views.deleteSkill, name='delete-skill'),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>/', views.view_message, name='message'),
    path('create-message/<str:pk>/', views.create_message, name='create-message'),
]