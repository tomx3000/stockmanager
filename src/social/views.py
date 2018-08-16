from django.shortcuts import render

# Create your views here.

def socialSample(request,*args,**kargs):
	
	return render(request,'social.html',{})

