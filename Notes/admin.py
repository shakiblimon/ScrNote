from django.contrib import admin

# Register your models here.
from Notes.models import Term, Course, ClassNote

admin.register(Term)
admin.register(Course)
admin.register(ClassNote)