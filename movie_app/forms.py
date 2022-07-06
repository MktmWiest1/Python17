from django import forms
from . import models


class DirectorForm(forms.ModelForm):
    class Meta:
        model = models.Director
        fields = '__all__'


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = '__all__'
