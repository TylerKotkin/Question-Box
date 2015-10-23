from django.conf.urls import url
from . import views as qviews


urlpatterns = [
    url(r'^user/(?P<pk>\w+)$', qviews.UserListView.as_view(), name='user_detail'),
    url(r'^question/$', qviews.QuestionListView.as_view(), name='all_questions'),
    url(r'^question/ask$', qviews.ask_question, name='ask_question'),
    url(r'^$', qviews.home, name='home'),
    ]
