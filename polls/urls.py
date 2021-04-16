from django.urls import path, include
from rest_framework.routers import DefaultRouter

from polls.views import PollViewSet, QuestionViewSet, index, UserAnswerViewSet, UserAnswerListView

router = DefaultRouter()
router.register(r'polls', PollViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', UserAnswerViewSet)

urlpatterns = [
    path('', index),
    path('api/', include(router.urls)),
    path('api/answer-list/', UserAnswerListView.as_view()),
]
