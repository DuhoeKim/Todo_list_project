from django.urls import path
from . import views
app_name = 'lists'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete', views.delete, name='delete'),
]
