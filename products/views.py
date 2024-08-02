from rest_framework.views import APIView
from .models import Post as PostModel
from .models import Request as RequestModel
from .serializers import PostSerializer, RequestSerializer, RequestDetailSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

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
    def get(self, request, user_id):
        requests = RequestModel.objects.filter(user_id=user_id).select_related('post')

        if not requests.exists():
            raise NotFound("이 사용자에 대한 요청을 찾을 수 없습니다")
        
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

class RequestPostView(APIView):
    def post(self, request, user_id, post_id):
        try:
            post = PostModel.objects.get(post_id=post_id)
        except PostModel.DoesNotExist:
            raise NotFound("해당 포스트를 찾을 수 없습니다.")

        data = request.data.copy()
        data['user'] = user_id
        data['post'] = post_id 

        serializer = RequestDetailSerializer(data=data)
        if serializer.is_valid():
            request_instance = serializer.save()
            return Response(RequestDetailSerializer(request_instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)