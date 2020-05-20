from .views import article_list, article_detail, ArticleApiView, ArticleDetails
from django.urls import path, include

urlpatterns = [
    # path('article/',article_list,name = 'article_list'),
    path('article/', ArticleApiView.as_view(), name='article_list'),
    # path('detail/<int:pk>/', article_detail, name='article_detail'),
    path('detail/<int:id>/', ArticleDetails.as_view(), name='article_detail'),
]
