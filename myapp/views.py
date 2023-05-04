from django.shortcuts import render,redirect
from.forms import imageform
from django.http import HttpResponse
def index(request):
    if request.method=='POST':
        myform=imageform(request.POST,request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('image')
        return redirect('index')
    else:
        myform=imageform()
        return render(request,'home.html',{'form':myform})
def home(request):
    return  HttpResponse("iMAGE UPLOADED SAUCCESSFULLY")



# Create your views here.
