from django.urls import path
from .views import *  # импортируем наше представление

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail'),
]