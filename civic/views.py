from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import EmailTemp, Address
from .forms import EmailForm, AddressForm
import requests
# Create your views here.
def index(request):
    return render(request, 'civic/index.html', {})

def submit(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            #form.approved = False
            #form.sender = request.user.username
            form.save()
            sub = EmailTemp.objects.last()
            sub.sender = request.user.username
            sub.save()

    form = EmailForm()
    return render(request, 'civic/submit.html', {'form': form})

def search(request):
    allTemps = EmailTemp.objects.all()
    return render(request, 'civic/allTemps.html', {'allTemps':allTemps})

def userpage(request):
    allTemps = EmailTemp.objects.all()
    return render(request, 'civic/userTemps.html', {'allTemps':allTemps})

def rep(request):
    return render(request, 'civic/rep.html', {})

def resources(request):
    return render(request, 'civic/resources.html', {})

def find(request):
    key = "AIzaSyC6fQl0ZvuPjVzX65zhZzvww_vj56EvmTk"
    getRep = "https://www.googleapis.com/civicinfo/v2/representatives?key=" + key + "&address="
    form = AddressForm(request.POST)
    resp = ""
    addr2 = ""
    if form.is_valid():
        form.save()
        addr = Address.objects.last().address
        resp = addr
        spl = resp.split()
        addr2 = addr
        addr = ""
        for x in spl:
            x = x.replace(',', '')
            addr += x + "%20"
        getRep += addr[:-3]
        resp = requests.get(getRep).json()
        Address.objects.all().delete()
        #print(type(resp))
    form = AddressForm()
    return render(request, 'civic/find.html', {'form':form, 'resp':resp, 'addr':addr2})
