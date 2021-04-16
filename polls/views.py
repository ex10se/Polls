from rest_framework import viewsets

from polls.models import Poll, Question
from polls.serializers import PollSerializer, QuestionSerializer


class PollViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    # permission_classes = []


class QuestionViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = []
