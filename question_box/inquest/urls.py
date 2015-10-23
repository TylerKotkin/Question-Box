from django.conf.urls import url
from . import views as qviews


urlpatterns = [
    url(r'^user/(?P<pk>\w+)$', qviews.UserListView.as_view(), name='user_detail'),
    url(r'^question/$', qviews.QuestionListView.as_view(), name='all_questions'),
    url(r'^question/ask$', qviews.ask_question, name='ask_question'),
    url(r'^answer/(?P<pk>\w+)$', qviews.AnswerListView.as_view(), name='answer_list'),
    url(r'^answer/add/(?P<question_id>\d+)$', qviews.add_answer, name='add_answer'),
    url(r'^$', qviews.home, name='home'),
    ]
