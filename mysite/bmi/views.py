from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"blog/index.html")

def add(request):
    try:
        vazn=int(request.GET["vazn"])
        ghad=int(request.GET["ghad"])
        ghad=ghad/100
        ghad2=ghad*ghad
        sum=vazn/ghad2
        result = format(sum, '.1f')
        new_result=float(result)
    except ValueError:
            return render(request,"blog/index.html",{"res":"eroor"})
    
    if new_result<19:
        return render(request,"blog/index.html",{"res":result})
    elif 19<new_result<25:
        return render(request,"blog/index.html",{"res":result})
    else:
        return render(request,"blog/index.html",{"res":result})