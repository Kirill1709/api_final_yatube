from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, PostViewSet, GroupList, FollowList

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/group/', GroupList.as_view()),
    path('v1/follow/', FollowList.as_view()),
]
