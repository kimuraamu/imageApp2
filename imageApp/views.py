from django.shortcuts import render, redirect
from .models import Document
from django import forms
from .forms import DocumentForm
from PIL import Image
 
def index(request):
        if request.method != 'POST':
            form = DocumentForm()
            #obj = Document.objects.latest("uploaded_at")
        else:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                photo = form.cleaned_data['photo']
                document = Document()
                document.photo = photo
                document.save()
                obj = Document.objects.latest("uploaded_at")
        
        context = {
            'form': form,
            'obj': obj
        }
        return render(request, 'imageApp/model_form_upload.html', context)