from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Photo, Post
from .serializers import PostSerializer, PhotoSerializer
from rest_framework import viewsets


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all().order_by("id")
    serializer_class = PostSerializer


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Photo.objects.all().order_by("id")
    serializer_class = PhotoSerializer


@api_view(['GET', "POST"])
def post(request):
    if request.method == 'GET':
        id = request.GET.get("id", "")
        try:
            post = Post.objects.get(key=id)
        except Post.DoesNotExist:
            error = {
                "error": {
                    "errors": [
                        {
                            "domain": "global",
                            "reason": "Post notFound",
                            "message": "Not Found"
                        }
                    ],
                    "code": 404,
                    "message": "Not Found"
                }
            }
            return JsonResponse(error, safe=False)
        response = {
            'title': post.title,
            'owner': post.owner,
            'caption': post.caption,
            'date': post.date,
            'is_carousel_item': post.is_carousel_item,
            'media_type': post.media_type,
            'status': post.status,
            'thumb_offset': post.thumb_offset,
            'access_token': post.access_token,
            'ig_user_id': post.ig_user_id,
        }
        return JsonResponse(response, safe=False)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)


@api_view(['GET', "POST"])
def photo(request):
    if request.method == 'GET':
        id = request.GET.get("id", "")
        try:
            photo = Photo.objects.get(key=id)
        except Photo.DoesNotExist:
            error = {
                "error": {
                    "errors": [
                        {
                            "domain": "global",
                            "reason": "Photo notFound",
                            "message": "Not Found"
                        }
                    ],
                    "code": 404,
                    "message": "Not Found"
                }
            }
            return JsonResponse(error, safe=False)
        response = {
            "id": photo.id,
            "title": photo.title,
            "url": photo.url,
            "post": photo.post
        }
        return JsonResponse(response, safe=False)
    elif request.method == 'POST':
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)
