from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"Templateapp1/html1.html")
def add(request):
    val1=int(request.GET["n1"])
    val2=int(request.GET["n2"])
    res=val1+val2
    return render(request,"Templateapp1/result.html",context={"result":res})