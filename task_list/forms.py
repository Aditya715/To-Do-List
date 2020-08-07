from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    """
        Add Task Django form.
    """

    # putting up placeholder in schedule field
    schedule = forms.DateField(widget=forms.DateInput
                    (attrs={'placeholder': 'YYYY-MM-DD'})
                )
    
    
    class Meta:
        model = Task
        fields = ['task', 'schedule']