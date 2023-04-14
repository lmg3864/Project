
from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    genre_choices = [('스릴러', '스릴러'),('공포','공포'),('액션','액션'),('로맨스','로맨스')]
    genre = forms.ChoiceField(choices = genre_choices, required = True)
    score = forms.FloatField(max_value=5,min_value=0,widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "0.5"}))
    release_date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    class Meta:
        model = Movie
        fields = '__all__'