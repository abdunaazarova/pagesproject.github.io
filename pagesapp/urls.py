from django.urls import path
from .views import HomePageView, AboutPageView, NewsPageView, ArticlesPageView

urlpatterns = [
    path('news/', NewsPageView.as_view(), name='news'),
    path('articles/', ArticlesPageView.as_view(), name='articles'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('', HomePageView.as_view(), name='home'),
]
