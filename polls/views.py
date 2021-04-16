from django.http import HttpResponseRedirect
from django.utils import timezone
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import Poll, Question, UserAnswer
from polls.permissions import ActionBasedPermission
from polls.serializers import PollSerializer, QuestionSerializer, UserAnswerSerializer, UserAnswerListSerializer


def index(request):
    # polls = Poll.objects.all()
    # return render(request, 'index.html', {'polls': polls})
    return HttpResponseRedirect('swagger')


class PollViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с опросами

    Get для всех, остальные запросы для администратора
    """

    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [ActionBasedPermission]
    action_permissions = {
        IsAdminUser: ['update', 'partial_update', 'destroy', 'create'],
        AllowAny: ['list', 'retrieve']
    }

    def list(self, request, *args, **kwargs):
        # вывод всех опросов для администратора
        if request.user.is_superuser:
            return super().list(self, request, *args, **kwargs)
        # вывод только активных опросов для пользователей
        queryset = self.filter_queryset(Poll.objects.filter(end_date__gte=timezone.now()))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с вопросами опросов

    Запросы для администратора
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]


class UserAnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с ответами вошедшего пользователя,
    либо всех пользователей, если авторизован администратор

    Get и post для всех, остальные запросы для администратора
    """

    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = [ActionBasedPermission]
    action_permissions = {
        IsAdminUser: ['update', 'partial_update', 'retrieve', 'destroy'],
        AllowAny: ['list', 'create']
    }

    def list(self, request, *args, **kwargs):
        # вывод всех ответов для администратора
        if request.user.is_superuser:
            return super().list(self, request, *args, **kwargs)
        # вывод только актуальных для пользователя ответов
        queryset = self.filter_queryset(UserAnswer.objects.filter(user=request.user.id))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserAnswerListView(APIView):
    """
    API endpoint для получения списка ответов пользователя

    Post для всех
    """

    @swagger_auto_schema(request_body=UserAnswerListSerializer)
    def post(self, request):
        user_answer = UserAnswer.objects.filter(user=request.data['user_id'])
        serializer = UserAnswerSerializer(data=user_answer, many=True)
        serializer.is_valid()
        return Response(serializer.data)
