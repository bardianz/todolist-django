from django import forms
from .models import ToDoItem

class ToDoItemAddForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title','description','checked']

class ToDoItemEditForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title','description','checked']
