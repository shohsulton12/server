from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(prefix='users', viewset=views.UserAccountViewSet, basename='users')
router.register(prefix='posts', viewset=views.PostViewSet, basename='post')
router.register(prefix='comments', viewset=views.CommentViewSet, basename='comment')


urlpatterns = router.urls

