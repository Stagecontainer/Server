from rest_framework import serializers
from .models import Post, Request

class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'post_id', 'company', 'purpose', 'category', 'address',
            'title', 'content', 'content_img', 'images', 'promotion',
            'logo_img', 'price', 'company_num', 'company_img', 'user'
        )
    
    def get_images(self, obj):
        # 이미지 필드들을 배열로 반환
        image_fields = [obj.image1, obj.image2, obj.image3, obj.image4, obj.image5]
        # 각 이미지 필드가 None이면 빈 문자열로 처리
        return [image.url if image else '' for image in image_fields]

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