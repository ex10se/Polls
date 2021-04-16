from rest_framework import serializers

from .models import Poll, Question


class PollSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    @staticmethod
    def get_questions(obj):
        return Question.objects.filter(poll=obj).values()

    class Meta:
        model = Poll
        fields = ('title', 'start_date', 'end_date', 'description', 'questions')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('poll', 'text', 'type')
