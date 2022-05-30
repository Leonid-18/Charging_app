from .serializers import LoginTokenObtainSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.http import JsonResponse
from rest_framework import views


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginTokenObtainSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_description = User.objects.get(pk=request.user.id)
        serializer_user = UserSerializer(user_description)
        return JsonResponse(serializer_user.data, status=status.HTTP_200_OK)
