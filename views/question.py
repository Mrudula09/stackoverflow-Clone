from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from stackoverflowApp.models import Question,User
from django import forms
from django.utils.translation import ugettext_lazy as _

from django.http.request import HttpRequest

class AddQuestion(ModelForm):
    class Meta:
        model = Question
        exclude = ['id','user','likes','tags']
        fields = ('title','description')
        widgets = {
            'title': forms.Textarea(attrs={'cols': 80, 'rows': 1}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 15}),
        }

class QuestionsList(ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'

    def get_context_data(self, *, object_list=None, **kwargs):
        contest = super(QuestionsList,self).get_context_data(**kwargs)
        return contest

class AskQuestion(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Question
    template_name = 'ask_question.html'
    form_class = AddQuestion
    success_url = reverse_lazy('question_list')

    def get_context_data(self, **kwargs):
        context = super(AskQuestion, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        user = self.request.user
        question_form = AddQuestion(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.user = user
            question.save()
        return redirect('question_list')

def GetQuestion(request):
    if request.method == 'GET':
        key = request.GET['key']
        questions = Question.objects.filter(title__icontains=key)
        return HttpResponse(list(questions))
    else:
        return HttpResponse("Failed")