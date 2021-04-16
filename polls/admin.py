from django.contrib import admin

from . import models


class QuestionInlineAdmin(admin.TabularInline):
    model = models.Question


@admin.register(models.Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'description')
    search_fields = ('id', 'title')
    inlines = (QuestionInlineAdmin,)


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('poll', 'text', 'type')
    search_fields = ('id', 'poll', 'text')
    list_filter = ('poll',)


@admin.register(models.UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    pass
