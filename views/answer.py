from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from stackoverflowApp.models import *

class AddAnswer(ModelForm):
    class Meta:
        model = Answer
        exclude = ['id', 'user', 'question']
        fields = ('description',)

class AnswerQuestion(CreateView):
    model = Answer
    template_name = 'answer_question.html'
    form_class = AddAnswer
    success_url = reverse_lazy('question_list')

    def get_context_data(self, **kwargs):
        context = super(AnswerQuestion, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
       user = self.request.user
       question = Question.objects.get(pk=kwargs.get('pk'))
       answer_form = AddAnswer(request.POST)

       if answer_form.is_valid():
           answer = answer_form.save(commit=False)
           answer.user = user
           answer.question = question
           answer.save()
       return redirect('answer_list',question.id)

class AnswerList(ListView):
    model = Answer
    template_name = 'answers.html'
    context_object_name = 'answers'

    def get_context_data(self, *, object_list=None, **kwargs):
        contest = super(AnswerList, self).get_context_data(**kwargs)
        contest['answers'] = self.model.objects.all().filter(question_id=self.kwargs.get('pk'))
        contest['question'] = Question.objects.get(id=self.kwargs.get('pk'))
        contest['comment'] = Comment.objects.all().filter(question_id=self.kwargs.get('pk'),answer_id=self.kwargs.get('pk'))
        likes=[]
        res= Like.objects.values('answer_id').filter(user_id=self.request.user.id)
        for i in res:
            likes.append(i['answer_id'])

        contest['like']=likes
        print(contest['like'])
        return contest

def AnswerQ(request):
    if request.method == 'GET':
        qid = request.GET['question_id']
        answer = request.GET['answer']
        print(qid)
        print(answer)
        ans = Answer(description=answer,question_id=qid,user_id=request.user.id)
        ans.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Failed")

def likePost(request):
    if request.method == 'GET':
        answerId = request.GET['answer_id']
        userId = request.GET['user_id']
        print(userId)
        like=Like(answer_id=answerId,user_id=request.user.id)
        like.save()
        no_of_likes = Answer.objects.get(id=answerId)
        no_of_likes.likes = no_of_likes.likes + 1
        no_of_likes.save()
        user = UserProfile.objects.get(user_id=userId)
        user.reputation = user.reputation + 10
        user.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Failed")

def unlikePost(request):
    if request.method == 'GET':
        answerId = request.GET['answer_id']
        userId = request.GET['user_id']
        print(userId)
        like=Like(answer_id=answerId,user_id=request.user.id)
        like.save()
        no_of_likes = Answer.objects.get(id=answerId)
        no_of_likes.likes = no_of_likes.likes - 1
        no_of_likes.save()
        user = UserProfile.objects.get(user_id=userId)
        user.reputation = user.reputation - 2
        user.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Failed")