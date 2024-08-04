from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
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

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            return Response(data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({
                "errors": serializer.errors,
                "message": "로그인에 실패했습니다."
            }, status=status.HTTP_400_BAD_REQUEST)

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({'nickname': user.nickname}, status=status.HTTP_200_OK)

class GetUserIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        nickname = request.query_params.get('nickname')
        if not nickname:
            return Response({"error": "사용자 닉네임이 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(nickname=nickname)
            return Response({'id': user.id}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
