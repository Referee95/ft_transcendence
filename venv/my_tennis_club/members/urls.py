from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members),
    path('members/details/<int:id>', views.details),
    path('details/<int:id>', views.details),
]