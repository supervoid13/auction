from django import forms
from .models import Lot, LotSection, LotComment


# class LotForm(forms.Form):
#     title = forms.CharField(max_length=100, label='Название лота')
#     description = forms.CharField(widget=forms.Textarea, label='Расскажите о вашем лоте')
#     section = forms.ChoiceField(choices=LotSection.objects.all())
#     starting_price = forms.FloatField(required=False, label='Стартовая цена')


class LotForm(forms.ModelForm):
    class Meta:
        model = Lot
        fields = [
            'title',
            'description',
            'section',
            'starting_price',
            'image',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Расскажите о своём лоте', 'class': 'form-control'}),
        }
        labels = {
            'title': 'Что вы хотите выставить на аукцион?',
            'description': 'Описание',
        }


class LotCommentForm(forms.ModelForm):
    class Meta:
        model = LotComment
        fields = [
            'text',
        ]
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Текст комментария'})
        }
