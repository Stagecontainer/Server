from rest_framework.serializers import ModelSerializer
from .models import Post, PostImage, Request

class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']

class PostSerializer(ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)  # PostImageSerializer를 nested serializer로 사용

    class Meta:
        model = Post
        fields = "__all__"

class RequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"