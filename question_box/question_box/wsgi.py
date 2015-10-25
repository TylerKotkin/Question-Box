"""
WSGI config for question_box project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
<<<<<<< HEAD

=======
# from dj_static import Cling
>>>>>>> a77637fff41b7e3d162e1788b237da607aec786c

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todomvc.settings")

application = DjangoWhiteNoise(get_wsgi_application())
<<<<<<< HEAD
=======
# application = Cling(get_wsgi_application())
>>>>>>> a77637fff41b7e3d162e1788b237da607aec786c
