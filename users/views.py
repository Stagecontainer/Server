from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import ValidationError
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from .models import User

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
                "nickname": user.nickname,
                "message": "회원가입이 완료되었습니다."
            }, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            # Check if the error is due to a unique constraint on nickname
            if 'nickname' in serializer.errors and any(
                'unique' in error for error in serializer.errors['nickname']
            ):
                return Response({
                    "errors": serializer.errors,
                    "message": "이미 사용중인 닉네임입니다."
                }, status=status.HTTP_400_BAD_REQUEST)
            return Response({
                "errors": serializer.errors,
                "message": "회원가입에 실패했습니다."
            }, status=status.HTTP_400_BAD_REQUEST)

class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
