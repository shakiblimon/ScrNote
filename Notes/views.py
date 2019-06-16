from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from Notes.models import Term, ClassNote
from Notes.serializers import TermSerializer, CourseSerializer


class TermViewSet(viewsets.ModelViewSet):
    serializer_class = TermSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        active_user = self.request.user
        if active_user.is_authenticated:
            queryset = Term.objects.filter(user=active_user)
        else:
            queryset = Term.objects.none()

        return queryset


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        active_user = self.request.user
        if active_user.is_authenticated:
            queryset = ClassNote.objects.filter(user=active_user)
        else:
            queryset = ClassNote.objects.none()
        return queryset
    