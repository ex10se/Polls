from rest_framework import serializers
from .models import Poll, Question, UserAnswer


class PollSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    @staticmethod
    def get_questions(obj):
        return Question.objects.filter(poll=obj).values()

    class Meta:
        model = Poll
        fields = ('title', 'id', 'start_date', 'end_date', 'description', 'questions')


class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Question
        fields = ('id', 'poll', 'text', 'type')


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ('user', 'poll', 'question', 'answer')


class UserAnswerListSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
