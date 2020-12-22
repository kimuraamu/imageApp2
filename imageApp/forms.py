from django import forms
from .models import Document
from PIL import Image
 
 
class DocumentForm(forms.Form):
    photo = forms.ImageField(required=True) #required=Trueで空の送信を防ぐ


