from django.shortcuts import render
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.timezone import make_aware
from question_box.forms import AnswerForm, UserForm, QuestionForm
from django.db.models import Count
from django.views import generic
from .models import Question, Answer
from django.contrib.auth.decorators import login_required

# Create your views here.


class UserListView(generic.ListView):
    template_name = 'inquest/user_detail.html'
    context_object_name = 'questions'
    paginate_by = 25

    def get_queryset(self):
        self.user = get_object_or_404(User, pk=self.kwargs['pk'])
        return self.user.question_set.all().order_by('-timestamp') \
            .prefetch_related('user')


class QuestionListView(generic.ListView):
    template_name = 'question_list.html'
    context_object_name = 'questions'
    paginate_by = 25

    model = Question

    def get_queryset(self):
        preload = Question.objects.all()
        return preload.order_by('-timestamp')


class AnswerListView(generic.ListView):
    template_name = 'answer_list.html'
    context_object_name = 'answer'
    paginate_by = 25
    model = Answer

    def get_context_data(self, **kwargs):
        context = super(AnswerListView, self).get_context_data(**kwargs)
        context['question'] = Question.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        preload = Answer.objects.all()
        return preload.order_by('-timestamp')


def home(request):
    return render(request, 'inquest/home.html')


@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.timestamp = make_aware(datetime.now())
            question.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Question posted.')
            return redirect('all_questions')

        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Form data invalid.')

    else:
        form = QuestionForm()
    return render(request,
                  'inquest/ask_question.html',
                  {'form': form})


@login_required
def add_answer(request, question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = Question.objects.get(pk=question_id)
            answer.timestamp = make_aware(datetime.now())
            answer.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Answer posted.')

        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Form data invalid.')

    else:
        form = QuestionForm()
    return render(request,
                  'inquest/answer_list.html',
                  {'form': form, 'question': Question.objects.get(pk=question_id)})




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('all_questions')
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
            return redirect('all_questions')
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
        return redirect('all_questions')
