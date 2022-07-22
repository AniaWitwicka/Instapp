from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"photos", views.PhotoViewSet)
router.register(r"posts", views.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(r"post/", views.post),
    path(r"photo/", views.photo)
]