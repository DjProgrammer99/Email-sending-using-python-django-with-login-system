from django.conf import settings
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm


def login_page(request):
    if request.method=='POST':
        uname =request.POST.get("username")
        passw = request.POST.get("password") 
        
        if(uname=="naresh" and passw=="jogu123"):
            fmsg="username :"+uname +' '+"password: "+passw
            m={'fmsg':fmsg}
            return redirect('/sendmail')
        else:
            fmsg='username :'+uname +' '+'password: '+passw
            # error_msg='Oops! username or password is incorrect'
            m={'fmsg':fmsg,'error_msg':error_msg}
            return render(request,'home.html',m) 
    else:
        error_msg='Oops! username or password is incorrect'
        m={'error_msg':error_msg}
        return render(request,'home.html',m)
        
  
def add_mail(request):
    if request.method=='POST':
        to = request.POST.get('toemail')
        subject = request.POST.get('subject')
        messages = request.POST.get('messages')
        file = request.FILES.get('file')
        email = EmailMessage(subject,messages,'coder48@gmail.com',['mrnaresh695@gmail.com'])
        email.attach(file.name, file.read(), file.content_type)
        email.send()
        return redirect('/success')
    else:
        return render(request,'sendmail.html')
    
from .models import SendMail

def success(request):
    data = SendMail.objects.all()
    list={'data':data}
    return render(request,'success.html',list)

def logout_view(request):
    logout(request)
    return redirect('/')

def adduser(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserCreationForm()
        context = {'form':f}
        return render(request,'adduser.html',context)
    
    
