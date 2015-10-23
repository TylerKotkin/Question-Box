from django.shortcuts import render
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.timezone import make_aware
from question_box.forms import UserForm
from django.db.models import Count
from django.views import generic
from .models import Question, Answer
from django.contrib.auth.decorators import login_required

# Create your views here.


class UserListView(generic.ListView):
    template_name = 'inquest/user_detail.html'
    context_object_name = 'question'
    paginate_by = 25

    def get_queryset(self):
        self.user = get_object_or_404(User, pk=self.kwargs['pk'])
        return self.user.question_set.all().order_by('-timestamp') \
            .prefetch_related('user')


def home(request):
    return render(request, 'inquest/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'ERROR LOGGING IN!')
            return render(request,
                          'inquest/user_login.html',
                          {'username': username})
    else:
        return render(request, 'inquest/user_login.html')


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = form['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=user.username, password=password)
            login(request, user)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Your account was successfully created.')
            return redirect('/')
    else:
        form = UserForm()
    return render(request,
                  'inquest/user_register.html',
                  {'form': form})


def user_logout(request):
    if request.user.is_authenticated():
        user_name = request.user.username
        logout(request)
        messages.add_message(request, messages.SUCCESS,
                             "{}, you have successfully logged out".format(
                                 user_name))
        return redirect('/')
