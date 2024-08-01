from rest_framework.serializers import ModelSerializer
from .models import Post, PostImage, Request, ReferenceImage

class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image_id', 'image']

class PostSerializer(ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)  # PostImageSerializer를 nested serializer로 사용

    class Meta:
        model = Post
        fields = "__all__"

class ReferenceImageSerializer(ModelSerializer):
    class Meta:
        model = ReferenceImage
        fields = ['refer_id', 'image']

class RequestSerializer(ModelSerializer):
    post = PostSerializer()
    referimages = ReferenceImageSerializer(many=True, read_only=True)

    class Meta:
        model = Request
        fields = "__all__"