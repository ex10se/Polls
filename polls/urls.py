from django.urls import path

from polls.views import PollView

urlpatterns = [
    path('', PollView.as_view()),
]
