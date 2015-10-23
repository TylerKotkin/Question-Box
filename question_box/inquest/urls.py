from django.conf.urls import url
from . import views as qviews


urlpatterns = [
    url(r'^user/(?P<pk>\w+)$', qviews.UserListView.as_view(), name='user_detail'),
    url(r'^$', qviews.home, name='home'),
    ]
