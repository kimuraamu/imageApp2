from django.shortcuts import render, redirect
from .models import Document
from django import forms
from .forms import DocumentForm
 
 
def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
        obj = Document.objects.all()
 
    return render(request, 'imageApp/model_form_upload.html', {
        'form': form,
        'obj': obj
    })