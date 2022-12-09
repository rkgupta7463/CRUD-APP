from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('<int:uid>/update/', update, name="update"),
    path('<int:pk>/delete/', delete, name="delete"),
]
