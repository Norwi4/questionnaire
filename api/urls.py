from django.urls import path, include

from api.admin import AdminPolls, AdminPollById, AdminQuestions, AdminQuestionById
from api.views import Polls, PollById, PollsByUser

urlpatterns = [
    path('polls', Polls.as_view()),
    path('polls/<int:id>', PollById.as_view()),
    path('pollsByUser/<int:id>', PollsByUser.as_view()),
    

]

