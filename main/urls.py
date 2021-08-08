from django.urls import path, include
from . import views


app_name = 'main'


urlpatterns = [
    # Домашняя страница.
    path('', views.index, name='index'),

]
