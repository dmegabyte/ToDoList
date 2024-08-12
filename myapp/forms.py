from django import forms
from.models import User


from django import forms
from .models import Todo



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'text','colour','deadline']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'colour': forms.RadioSelect(choices=Todo.COLOUR_CHOICES, attrs={'class': 'form-control'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
        }

