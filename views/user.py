from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView
from django import forms
from django.core.files.images import get_image_dimensions
from django.shortcuts import redirect
from stackoverflowApp.models import UserProfile,User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['id','user_id']
        fields = ('profile_image','place','college','degree')

class Profile(CreateView):
    model = UserProfile
    template_name = 'create_profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('question_list')

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile_form =UserProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('question_list')


class updateProfile(UpdateView):
    model = UserProfile
    template_name = 'create_profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('view_profile')


class ViewProfile(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = UserProfile
    template_name = 'viewProfile.html'
    context_object_name = 'profile'

    def get_context_data(self, *, object_list=None, **kwargs):
        contest = super(ViewProfile, self).get_context_data(**kwargs)
        contest['profile'] = self.model.objects.get(user_id=self.request.user.id)
        contest['user'] = User.objects.get(id=self.request.user.id)
        return contest

class Users(ListView):
    model = UserProfile
    template_name = 'users.html'
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        contest = super(Users, self).get_context_data(**kwargs)
        contest['users'] = self.model.objects.all()
        return contest