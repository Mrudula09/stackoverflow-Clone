from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from django import forms
from django.shortcuts import redirect
from stackoverflowApp.models import User,Tag

class CreateTag(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = ['id']
        fields = ('name','information')

class AddTag(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Tag
    template_name = 'addTag.html'
    form_class = CreateTag
    success_url = reverse_lazy('tag_list')

class TagList(ListView):
    model = Tag
    template_name = 'tags.html'
    context_object_name = 'tags'

    def get_context_data(self, *, object_list=None, **kwargs):
        contest = super(TagList, self).get_context_data(**kwargs)
        contest['tags'] = self.model.objects.all()
        return contest
