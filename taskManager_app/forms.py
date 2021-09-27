from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'})
    )
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'})
    )

    class Meta:
        model = Task
        fields = ('title', 'description')
