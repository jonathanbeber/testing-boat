from django import forms

from lists.models import Item

class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(
                attrs={
                    'placeholder' : 'insert a new item',
                    'class': 'text-center form-control input-lg'
                }
            )
        }
