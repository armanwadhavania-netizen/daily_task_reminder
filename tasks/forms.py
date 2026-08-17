from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'email',
            'due_date',
            'due_time',
        ]

        widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'due_time': forms.TimeInput(
                attrs={'type': 'time'}
            ),
        }