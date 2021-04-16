from django.urls import path, include
from rest_framework.routers import DefaultRouter

from polls.views import PollViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'polls', PollViewSet, basename='polls')
router.register(r'questions', QuestionViewSet, basename='questions')

urlpatterns = [
    path('', include(router.urls)),
]
