from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from . import serializers, models


class SignupUser(APIView):
    @extend_schema(responses=serializers.UserSerializer)
    def post(self, request, **kwargs):
        serializer = serializers.UserSerializer(
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            user = serializer.instance
            user.set_password(request.data["password"])
            user.save()
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "token": token.key
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    @extend_schema(responses=serializers.UserSerializer)
    def post(self, request, **kwargs):
        user = get_object_or_404(
            models.User,
            username=request.data["username"]
        )
        
        if not user.check_password(request.data["password"]):
            return Response(
                {"detail": "Not found."}, 
                status = status.HTTP_401_UNAUTHORIZED
            )
        
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            "token" : token.key
        })
        
class CurrentUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @extend_schema(responses=serializers.UserSerializer)
    def get(self, request, **kwargs):
        user_data = dict(
            serializers.UserSerializer(
                instance=request.user
            ).data
        )
        
        user_data.pop("password")
        
        return Response(user_data)

class UpdateUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @extend_schema(responses=serializers.UserSerializer)
    def put(self, request, **kwargs):        
        serializer = serializers.UserSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)