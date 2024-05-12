from django.forms import ModelForm

from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'text', 'important', 'completed']
        #fields = '__all__' # 全部欄位