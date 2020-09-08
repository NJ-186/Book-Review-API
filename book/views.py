from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer

from .models import Book
from rest_framework import authentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.backends import JWTAuthorAuthentication,JWTNormalUserAuthentication


# Create your views here.

@api_view(['GET'])
def overview(request):
    api_urls = {
        'List Books':'api/list-books',
        'Add':'api/author/add',
        'Search':'api/user/search',
        'Upvote':'api/user/upvote',
        'Comment':'api/user/comment',
    }

    return Response(api_urls)

@api_view(['GET'])
@authentication_classes([JWTNormalUserAuthentication])
@permission_classes([IsAuthenticated])
def listBook(request):
    book = Book.objects.all()
    serializer = BookSerializer(book,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JWTAuthorAuthentication])
@permission_classes([IsAuthenticated])
def add(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTNormalUserAuthentication])
@permission_classes([IsAuthenticated])
def search(request,pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book,many=False)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTNormalUserAuthentication])
@permission_classes([IsAuthenticated])
def upvote(request,pk):
    book = Book.objects.get(id=pk)
    book.upvotes = book.upvotes + 1
    book.save()
    return Response('Book Upvoted')

@api_view(['POST'])
@authentication_classes([JWTNormalUserAuthentication])
@permission_classes([IsAuthenticated])
def comment(request,pk):
    book = Book.objects.get(id=pk)
    
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    