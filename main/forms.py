from django import forms
from .models import TodoList

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check= forms.BooleanField(required=False)

class DeleteList(forms.Form):
    list_to_delete = forms.ModelChoiceField(queryset=TodoList.objects.all(), label="")







