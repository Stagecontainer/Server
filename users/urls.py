from django.urls import path
from .views import UserCreateView, LoginView, CurrentUserView, GetUserIdView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('current_user/', CurrentUserView.as_view(), name='current_user'),  # 현재 사용자 정보 엔드포인트 추가
    path('get_user_id/', GetUserIdView.as_view(), name='get_user_id'),  # 사용자 ID 조회 엔드포인트 추가
]