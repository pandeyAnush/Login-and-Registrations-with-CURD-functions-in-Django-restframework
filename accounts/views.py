from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from home.serializers import UserRegistrationSerializer
from home.serializers import UserLoginSerializer 
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken


class UserRegistrationView(APIView):
    def post(self, request, format = None):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'message': 'Registration successfully'},
            status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# class UserLoginView(APIView):
#     def post(self, request, format = None):
#             serializer = UserLoginSerializer(data = request.data)
#             if serializer.is_valid(raise_exception=True):
#                 email = serializer.data.get('email')
#                 password = serializer.data.get('password')
#                 user = authenticate(email=email, password=password)
#                 if user is not None:
#                     return Response({'message': 'Login successfully'},
#                     status = status.HTTP_200_OK)
#                 else:
#                     return Response({'errors': {'non_field_errors':['Email or Password is not valid']}}, status=status.
#                     HTTP_404_NOT_FOUND)
#             return Response(serializer.errors, status=status.
#                     HTTP_400_BAD_REQUEST)



def get_token(user):
    refresh = RefreshToken.for_user(user)
    update_last_login(None, user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserLoginView(APIView):

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                jwt_access_token = get_token(user)
                return Response({
                    'error': False,
                    'access_token': jwt_access_token['access'],
                    'refresh_token': jwt_access_token['refresh']
                }, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
