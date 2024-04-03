from django.shortcuts import render
from rest_framework.views import APIView
from .models import Post
from .serializers import EvlonPostSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class EvlonPostsView(APIView):
    def get(self, request):
        posts=Post.objects.all()
        serializer=EvlonPostSerializer(posts, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = EvlonPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
