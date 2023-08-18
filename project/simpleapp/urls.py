from django.urls import path
from .views import NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, ArticlesCreateView, ArticlesUpdateView, \
    ArticlesDeleteView, subscriptions

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticlesCreateView.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticlesUpdateView.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', ArticlesDeleteView.as_view(), name='articles_delete'),
    path('subscriptions/', subscriptions, name='subscriptions')

]