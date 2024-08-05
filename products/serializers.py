from rest_framework import serializers
from .models import Post, Request

class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'post_id', 'company', 'purpose', 'category', 'address', 'rating',
            'title', 'content', 'content_img', 'image1', 'image2', 'image3', 'image4', 'image5', 
            'promotion', 'logo_img', 'price', 'company_num', 'company_img', 'user', 'images'
        )

    def get_images(self, obj):
        # 이미지 필드들을 리스트로 반환하며, 값이 없으면 빈 문자열을 반환
        image_fields = ['image1', 'image2', 'image3', 'image4', 'image5']
        return [getattr(obj, field).url if getattr(obj, field) else '' for field in image_fields]

class RequestSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Request
        fields = "__all__"

class RequestDetailSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Request
        fields = "__all__"