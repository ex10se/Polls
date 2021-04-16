from django.contrib import admin

from . import models


@admin.register(models.Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'description')
    search_fields = ('id', 'title')


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    model = models.Poll
