from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    cate_choices = [('끄적끄적', '끄적끄적'),('고민상담','고민상담'),('정보','정보'),('수다','수다')]
    cate = forms.ChoiceField(choices = cate_choices, required = True)
    class Meta:
        model = Article
        fields = '__all__'
