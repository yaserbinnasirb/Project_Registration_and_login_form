from django.shortcuts import render
from django.http import HttpResponse
from .models import reglog
from django.views import View
class home(View):
    def get(self,request):
        return render(request,'home.html')
class regin(View):
    def get(self,request):
        return render(request,'regin.html')
class register(View):
    def post(self,request):
        r1 = reglog(username=request.POST['t1'],email=request.POST['t3'],password=request.POST['t6'],firstname=request.POST['t2'],lastname=request.POST['t8'],mobileno=request.POST['t4'],age=request.POST['t5'],gender=request.POST['t7'])
        r1.save()
        return HttpResponse('successfully registered')
class loginin(View):
    def get(self,request):
        return render(request,'loginin.html')
class login(View):
    def post(self,request):
        username = request.POST['t1']
        password = request.POST['t2']
        db= reglog.objects.filter(username=username,password=password)
        if not db:
            return HttpResponse('invalid username or password')
        else:
            return HttpResponse('successfully logged in')





