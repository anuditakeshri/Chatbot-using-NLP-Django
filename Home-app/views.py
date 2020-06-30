from django.shortcuts import render,redirect
from .models import messageItem
from .nlp import give_response

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def chatbot(request):
    all_message_items = messageItem.objects.all()
    return render(request, 'chat.html',{'all_message_items': all_message_items})

def addmsg(request):
    c = request.POST['content']
    new_item = messageItem(content = c)
    new_item.save()
    bot_msg(c)
    return redirect('chatbot')

def bot_msg(msg):
    c = give_response(msg)
    new_item = messageItem(content = c, isbot = True)
    new_item.save()
    return redirect('chatbot')
    