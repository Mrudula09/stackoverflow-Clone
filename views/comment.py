from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from stackoverflowApp.models import *

class AddComment(ModelForm):
    class Meta:
        model = Comment
        exclude = ['id', 'user', 'question','answer']
        fields = ('description',)

class CommentAnswer(CreateView):
    model = Comment
    template_name = 'comment_answer.html'
    form_class = AddComment
    success_url = reverse_lazy('question_list')

    def get_context_data(self, **kwargs):
        context = super(CommentAnswer, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
       user = self.request.user
       question = Question.objects.get(pk=kwargs.get('qid'))
       answer = Answer.objects.get(pk=kwargs.get('pk'))
       comment_form = AddComment(request.POST)

       if comment_form.is_valid():
           comment = comment_form.save(commit=False)
           comment.user = user
           comment.question = question
           comment.answer = answer
           comment.save()
       return redirect('answer_list',question.id)

def comment(request):
    if request.method == 'GET':
        qid = request.GET['question_id']
        aid = request.GET['answer_id']
        comment = request.GET['comment']
        print(qid)
        print(aid)
        print(comment)
        cmt = Comment(description=comment,answer_id=aid,question_id=qid,user_id=request.user.id)
        cmt.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Failed")