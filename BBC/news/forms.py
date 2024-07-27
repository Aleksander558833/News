from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)
    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'author']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title is not None and len(title) < 20:
            raise ValidationError({
                'title': 'Заголовок не может быть менее 20 символов.'
            })
        # text = cleaned_data.get('text')
        # if text is not None and len(text) < 20:
        #     raise ValidationError({
        #         'text': 'Текст не может быть менее 20 символов.'
        #     })
        return cleaned_data