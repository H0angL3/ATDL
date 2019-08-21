from django.shortcuts import render
from django.template.response import TemplateResponse
from . import forms
def index(request):
    textArea = forms.wordProcessForm()
    context = {'textArea': textArea}
    return TemplateResponse(request, 'baseBellLaPadula/base.html', context=context)

