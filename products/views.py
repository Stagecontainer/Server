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

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class PostDetailView(APIView):
    def get_object(self, post_id):
        posts = PostModel.objects.get(post_id=post_id)
        return posts

    def get(self, request, post_id):
        posts = self.get_object(post_id)
        serializer = PostSerializer(posts)
        return Response(serializer.data)

class RequestListView(APIView):
    def get_object(self, user_id):
        return RequestModel.objects.filter(user_id=user_id)

    def get(self, request, user_id):
        requests = self.get_object(user_id)
        if not requests.exists():
            raise NotFound("이 사용자에 대한 요청을 찾을 수 없습니다")
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)