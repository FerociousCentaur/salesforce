from django.shortcuts import render
import base64
import json
import requests
# Create your views here.
from django.conf import settings
from .forms import ArrayForm

def arrayPage(request):
    if request.method == 'POST':
        form = ArrayForm(request.POST)
        print(form.errors)
        if form.is_valid():
            array1 = (form.cleaned_data['array1']).split(' ')
            array2 = (form.cleaned_data['array2']).split(' ')
            print(array1,array2)
            processed_Data = processArray(array1, array2)
            return render(request, 'Homepage.html', {'form': form, 'response': processed_Data})
    return render(request, 'Homepage.html', {'form': ArrayForm})

def processArray(arr1,arr2):
    return arr1+arr2