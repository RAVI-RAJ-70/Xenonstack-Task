from django.shortcuts import render
from django.http import HttpResponse

def reg(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def pulsar(request):
    return render(request,'pulsar.html')

def ktm(request):
    return render(request,'ktm.html')

def passion(request):
    return render(request,'passion.html')

def sucessfully_regr(request):
    return render(request,'sucessfully_regr.html')

def thankyou(request):
    return render(request,'thankyou.html')

def contact_us(request):
    return render(request,'contact_us.html')

    from django.contrib.auth.decorators import login_required

#import model
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import reg

# Create your views here.


#contact-us  page  function
def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('cpassword')
        #password condition
        # if password == c_password:
        #     #email condition
        #     if User.objects.filter(username=username).exists():
        #         message.info(request,"this username is already taken")
        #         return redirect('/')
            
                
        #     else:
        #         user = User.objects.create_user(username=username,password=password)
        #         user.save()
        # else:
        #     message.info(request,"password not match")
        #     return redirect('/')
        
        #send data for model and store in database
        d = reg() # d:- means details of all data
        d.name=name
        d.username = username
        d.password=password
        d.c_password = c_password
        
        #save the object in databse
        d.save()
        # return redirect("login/")
    else:
        
        return render(request,'contactus.html')
  
    

#login pagefunction
def login(request):
    if request.method =='POST':
        user_name = request.POST['username']
        password = request.POST['password']
        
        #match username and password in database
        user = auth.authenticate(username = user_name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home/')
        else:
            messages.info(request,"login invalid")
            return redirect('/login/')
    else:
        
        return render(request,'login.html')

#logout

@login_required(login_url='login')  
def logout(request):
    auth.logout(request)
    return redirect('/')
    return render(request,'logout.html')
    


#home page  function
def home(request):
    return render(request,'home.html')



#all food product details function
def details(request):
    return render(request,"details.html")


def details2(request):
    return render(request,"details2.html")
def cong(request):
    return render(request,'payment.html')