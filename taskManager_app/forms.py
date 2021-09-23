from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'})
    )
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'})
    )

    class Meta:
        model = Tasks
        fields = ('title', 'description')
