from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from .serializers import *
from apps.app.models import *

from django.http import HttpResponse
from django.http import  HttpResponse

#user
class User_views_list(APIView):
    def get(self, request):
        user = ModelsUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = UserSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class User_views_detail(APIView):
    def get(self, request, pk):
        user = ModelsUser.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        user = ModelsUser.objects.get(p=pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        
        def delete(self, request, pk):
            user.delete()
            return Response(status=HTTP_204_NO_CONTENT)

#post
class Post_views_list(APIView):
    def get(self, request):
        post = ModelsPost.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = PostSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Post_views_detail(APIView):
    def get(self, request, pk):
        post = ModelsPost.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        post = ModelsPost.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = ModelsPost.objects.get(pk=pk)
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    

        