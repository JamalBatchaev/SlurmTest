from django import forms
from .models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "body", "due_date", "category")


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("body", "due_date", "is_done", "category")
