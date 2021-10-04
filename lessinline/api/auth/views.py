from django.contrib.auth import authenticate
from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lessinline.accounts.models import User
from .serializers import UserLoginSerializer, UserRegisterSerializer, UserProfileSerializer


@api_view(['POST'])
def login_view(request):
    email = request.data['email']
    password = request.data['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            serializer = UserLoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise Response('user not found', status=status.HTTP_404_NOT_FOUND)
    else:
        raise Response('email id or password entered in invalid', 401)


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.active_users.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
