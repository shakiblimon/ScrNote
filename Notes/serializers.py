from django.contrib.auth import get_user_model
from rest_framework import serializers

from Notes.models import Term, Course, ClassNote


class TermSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes Term instances into representations such as JSON.
    """

    def __init__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        if user.is_autherticated:
            self.fields['user'].queryset = get_user_model().objects.filter(username=user.username)
        else:
            self.fields['user'].queryset = get_user_model().objects.none()

    class Meta():
        model = Term
        fields = ('user', 'school', 'year', 'session', 'term_slug')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    """
    Dynamically filters term choices by limiting options to the terms related to the active user via foreign-key.
    """

    def __init__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        user = self.context['request'].user

        if user.is_autherticated:
            self.fields['user'].queryset = get_user_model().object.filter(username=user.username)
            self.fields['term'].queryset = Term.objects.filter(user=user)
        else:
            self.fields['term'].queryset = Term.objects.none()

    class Meta():
        model = Course
        fields = ('user', 'title', 'course_code', 'course_slug', 'term')


class ClassNoteSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes: ClassNote instances into representations such as
    JSON.
    """

    class Meta():
        model = ClassNote
        fields = ('user', 'title', 'body', 'note_slug', 'course')

    def __init__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        user = self.context['request'].user

        if user.is_autherticated:
            self.fields['user'].queryset = get_user_model().object.filter(username=user.username)
            self.fields['course'].queryset = Course.objects.filter(user=user)
        else:
            self.fields['course'].queryset = Course.objects.none()
