from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404



class UserViewSet(ViewSet):
    """
    A viewset for viewing and editing user instances
    """
    def list(self, request):
        permission_classes = (permissions.AllowAny,)
        queryset = get_user_model().objects.all()
        serializer_class = UserSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    def retrieve(self, request, pk=None):
        queryset = get_user_model().objects.all()
        user = get_object_or_404(queryset, pk=pk)
        if user:
            serializer_class = UserSerializer(user)
            return Response(data=serializer_class.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)



class User(APIView):
    """
    View to a new create user
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
