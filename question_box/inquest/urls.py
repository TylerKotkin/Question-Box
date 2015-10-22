from django.conf.urls import url
from . import views as qviews


urlpatterns = [
    url(r'^$', qviews.home, name='home'),
    ]
