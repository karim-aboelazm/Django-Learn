from django import forms
from .models import *
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        
    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post')
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.post = self.post
        if comment:
            comment.save()
        return comment
        