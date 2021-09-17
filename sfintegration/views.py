from django.shortcuts import render
import base64
import json
import requests
# Create your views here.
from django.conf import settings
from .models import Contacts
from django.shortcuts import render, redirect, HttpResponse



def homepage(request):
    contacts = Contacts.objects.all()
    if contacts:
        return render(request,'Homepage.html', {'contacts': contacts})
    return render(request,'Homepage.html')

def delete_records(request):
    Contacts.objects.all().delete()
    return redirect('homepage')

def refill(request):
    data = {
    'client_id': settings.CLIENT_ID,
    'client_secret':settings.SECRET_ID,
    'grant_type':'password',
    'username':settings.SDFC_USER,
    'password':settings.PASSWORD
    }

    response = requests.post(settings.URL, data=data)
    json_res = response.json()
    #print(json_res)
    access_token = json_res['access_token']
    auth = {'Content_type':'application/json',
    'Accept_Encoding':'gzip',
    'Authorization':"Bearer %s"% access_token}
    instance_url = json_res['instance_url']

    url2= instance_url+"/services/data/v45.0/query/"
    params =  {'q':'SELECT Id, LastName, FirstName FROM Contact ORDER BY LastName, FirstName'}
    res = requests.get(url2 ,headers=auth, params = params)
    r = res.json()
    #print(r)
    attrs = r['records']
    l = []
    for i in attrs:
        l.append(Contacts(sd_id=i['Id'],f_name=i['FirstName'],l_name=i['LastName']))
    Contacts.objects.bulk_create(l)
    return redirect('homepage')
