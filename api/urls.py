from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewset, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/',article_list,name = 'article_list'),
    path('article/', ArticleApiView.as_view(), name='article_list'),
    # path('detail/<int:pk>/', article_detail, name='article_detail'),
    path('detail/<int:id>/', ArticleDetails.as_view(), name='article_detail'),
    path('generic/article/<int:id>/', GenericAPiView.as_view(), name='generic_article'),
]
