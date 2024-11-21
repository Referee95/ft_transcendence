from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.register),
    # path('login/', views.login_view),
    # path('update_profile/', views.update_profile),
    path('profile_user/', views.profile_user),
   
]