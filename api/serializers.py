from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['title', 'author', 'email']
        fields = '__all__'














