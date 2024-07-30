from rest_framework.views import APIView
from .models import Post as PostModel
from .models import Request as RequestModel
from .serializers import PostSerializer, RequestSerializer
from rest_framework.response import Response

class PostListView(APIView):
    def get(self, request): # GET /products
        all_posts = PostModel.objects.all() # Posts 모델의 모든 데이터
        serializer = PostSerializer(all_posts, many=True) # serializer로 번역
        return Response(serializer.data) # 데이터 던져주기

class RequestListView(APIView):
    def get(self, request):
        all_requests = RequestModel.objects.all()
        serializer = RequestSerializer(all_requests, many=True)
        return Response(serializer.data)