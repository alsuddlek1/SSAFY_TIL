from rest_framework import serializers
from .models import Article, Comment


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('id',)
        read_only_fields = ('article',)

class ArticleListSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many=True, read_only=True)
    comment_count =serializers.IntegerField(source='comment.count', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'comments',)