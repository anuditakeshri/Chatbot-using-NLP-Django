from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from Home.models import messageItem

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('chatbot')
        else:
            messages.info(request,'invalid credentials!')
            return redirect('login')
        
    else:
        return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken!!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                  messages.info(request,'Email Taken!!')
                  return redirect('register')
            else:
                user = User.objects.create_user(username= username, email = email, password = password1, first_name= first_name, last_name= last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords Not Matching!!')
            return redirect('register')
        return redirect('/')        
    else:
        return render(request,"register.html")
    
    
def logout(request):
    all_message_items = messageItem.objects.all()
    for item in all_message_items:
        item.delete()
    auth.logout(request)
    return redirect('/')
    
