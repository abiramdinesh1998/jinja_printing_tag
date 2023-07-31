from django.shortcuts import render

# Create your views here.

def data_render(request):
    d = {'name':'subbu','age':90}
    return render(request,'data_render.html',context=d)

def ifelse(request):
    d = {'a':10,'b':20}
    return render(request,'ifelse.html',context=d)

def if_elif(request):
    d = {'a':10,'b':20,'c':50}
    return render(request,'if_elif.html',context=d)

def nested_if(request):
    d = {'a':100,'b':200,'c':50}
    return render(request,'nested_if.html',context=d)