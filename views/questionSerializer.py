from stackoverflowApp.models import *
from rest_framework import serializers,generics

class QuestionsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','title','description']


class QuestionsSerialiserView(generics.ListCreateAPIView):
    serializer_class = QuestionsSerialiser

    def get_queryset(self):
        return Question.objects.filter(title__icontains=self.kwargs['slug'])