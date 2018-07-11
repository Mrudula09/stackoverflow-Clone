from attr.filters import include
from django.contrib import admin
from django.urls import path
from stackoverflowApp.models import *
from views.user import *
from views.question import *
from views.answer import *
from views.auth import *
from views.comment import *
from views.tag import *
from views.questionSerializer import *

urlpatterns = [
    path('login/',loginView.as_view(),name="login_page"),
    path('signup/',signupView.as_view(),name="signup_page"),
    path('createProfile/',Profile.as_view(),name="create_profile"),
    path('questions/',QuestionsList.as_view(),name="question_list"),
    path('askQuestion/',AskQuestion.as_view(),name="ask_question"),
    path('answerQusetion/<int:pk>',AnswerQuestion.as_view(),name="answer_question"),
    path('answers/<int:pk>',AnswerList.as_view(),name="answer_list"),
    path('answer/<int:qid>/comment/<int:pk>',CommentAnswer.as_view(),name="comment"),
    path('logout/',logout_user,name="logout_page"),
    path('answerQ/',AnswerQ,name='answer'),
    path('likepost/',likePost,name='like'),
    path('unlikepost',unlikePost,name='unlike'),
    path('viewProfile/',ViewProfile.as_view(),name="view_profile"),
    path('updateProfile/<int:pk>',updateProfile.as_view(),name="update_profile"),
    path('users/',Users.as_view(),name="users"),
    path('addTag/',AddTag.as_view(),name="create_tag"),
    path('tags/',TagList.as_view(),name="tag_list"),
    path('questionsByKey/<slug:slug>',QuestionsSerialiserView.as_view(),name="key_list"),
    path('comment/',comment,name="comment")
]
