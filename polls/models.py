from django.db import models

QUESTIONS = (
    ('text', 'Ответ текстом'),
    ('single', 'Ответ с выбором одного варианта'),
    ('multiple', 'Ответ с выбором нескольких вариантов'),
)


class Poll(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Начало')
    end_date = models.DateTimeField(verbose_name='Конец')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.id} {self.title}'

    class Meta:
        verbose_name = 'опрос'
        verbose_name_plural = 'опросы'


class Question(models.Model):
    poll = models.ForeignKey(Poll, verbose_name='Опрос', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст вопроса')
    type = models.CharField(max_length=255, choices=QUESTIONS, verbose_name='Тип')

    def __str__(self):
        return f'{self.id} {self.text}'

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
