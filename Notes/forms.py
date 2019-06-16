from django import forms

from Notes.models import ClassNote


class SearchBarForm(forms.ModelForm):
    """
        Searchbar that allows users to look for a specific note by note-title.
    """

    def __init__(self, *args, **kwargs):
        """
        HTML widget modification
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        searchbar_styles = {
            "class": "form-control form-control-dark w-100",
            "placeholder": "Enter note title",
            "aria-label": "Search",
        }
        self.fields['title'].widget.attrs.update(searchbar_styles)
        self.fields['title'].label = ''

    class Meta():
        """
            Allows user to search for a specific note by its title.
        """
        model = ClassNote
        fields = ('title')
