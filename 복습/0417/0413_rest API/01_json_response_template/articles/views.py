from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status

from .models import Article, Comment
from django.core import serializers
from .serializers import ArticleSerializer, CommentSerializer

# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article.html', context)

def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id' : article.pk,
                'title' : article.title,
                'content' : article.content,
            }
        )
    return JsonResponse(articles_json, safe=False)
# articles_json 은 python의 list 이므로 JsonResponse 사용


def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    # json 형태로 articles를 serialize해줌
    return HttpResponse(data, content_type='application/json')
    # html 이 아닌 Http 로 연결해줌 


@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    serializers = ArticleSerializer(articles, many=True)
    return Response(serializers.data)

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    # else 안됨 ! 왜냐면 method가 너무 많아
    elif request.method == 'POST':
        # 역직렬화 (json을 python으로 받거나, ORM 을 이용해서 데이터를 넣음)
        serializer = ArticleSerializer(data=request.data) # serializer중에 데이터가 있는 serializer
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data) # 안받아주면 생성이랑 같음
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializers = CommentSerializer(comments, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def comment_detail(request, comment_pk):
    if request.method == 'GET':
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)