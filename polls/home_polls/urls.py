from django.urls import path
from . import views

app_name = 'home_polls'

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    path('results/<int:question_id>/', views.results, name='results'),
    path('vote/<int:question_id>/', views.vote, name='vote'),
]