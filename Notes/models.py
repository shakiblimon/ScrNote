from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Term(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='terms')
    school = models.CharField(max_length=20, blank=False)
    year = models.IntegerField(blank=False, null=True)
    session = models.CharField(max_length=40, blank=False)
    term_slug = models.SlugField(null=True)
    current = models.BigIntegerField(default=False)

    def __str__(self):
        return f'{self.session}'

    class Meta:
        ordering = ['-year']


class Course(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name='courses')
    terms = models.ForeignKey(Term, on_delete=models.CASCADE, null=True, related_name='courses')
    course_code = models.CharField(max_length=40, unique=True, blank=False)
    title = models.CharField(max_length=40, blank=False)
    course_slug = models.SlugField(null=True)

    def __str__(self):
        return f'{self.course_code}'

    class Meta:
        ordering = ['-course_code']


class ClassNote(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=False)
    body = RichTextField(config_name='ckeditor')
    note_slug = models.SlugField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='notes')

    def __str__(self):
        return f'{self.title}'

    def join_title(self):
        joined_title = ''.join(self.title.lower().split(' '))
        return joined_title

    class Meta:
        ordering = ['course', '-created_at']
