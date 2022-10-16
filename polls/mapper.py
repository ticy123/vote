from bpmappers.djangomodel import ModelMapper

from polls.models import Subject


class SubjectMapper(ModelMapper):
    class Meta:
        model = Subject
        exclude = ('is_hot',)