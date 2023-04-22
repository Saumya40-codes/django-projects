from django.shortcuts import render, redirect
from .models import Room,Message,Topic, Test, SignUp, Loginpage
from .forms import RoomForm, SignUpForm, TestForm,TopicForm, Loginform
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout , login as login_dj
from django.contrib import messages
# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    room = Room.objects.filter(
        Q(topic__name__icontains= q) | #only 'contains' is case sensitive matching
        Q(name__icontains= q) |
        Q(description__icontains= q)
        )   

    available_rooms = room.count()    
    topic = Topic.objects.all()
    context = {'rooms': room, 'topics': topic, 'top':Topic.objects.all(), 'available_rooms': available_rooms}
    return render(request, 'base/home.html', context)
 

def index(request,pk):
    room = Room.objects.get(id=pk)
    return render(request, 'base/room.html',{'room_name': room})

def nav(request):
    det = {'info': direc}
    return render(request, 'base/navbar.html', det)

direc =[
    {'name':'saumya', 'password':'lol'},
]


def createRoom(request):
    if(request.method == 'POST'):
        form = RoomForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('home')
    form = RoomForm()   
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def signUp(request):
    if(request.method == 'POST'):
            name = request.POST.get('user')
            email = request.POST.get('email')
            password = request.POST.get('password')
            form = SignUpForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('home')
    form = SignUpForm()
    context = {'form': form}
    return render(request, 'base/signup.html', context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/update_room.html', context)

# rooms = [
#     {'id': 1, 'name': 'index'},
#     {'id': 2, 'name': 'room2'},
#     {'id': 3, 'name': 'room3'},
#     {'id': 4, 'name': 'room4'},
# ]




def delete(request, pk):
    room= Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})

def testIt(request):
    if(request.method == 'POST'):
        form = TestForm(request.POST)
        if(form.is_valid()):
            print(form)
            return redirect('home')
        else:
            print(form.errors())
            return redirect('test')
    form = TestForm()
    context  = {'form':form}
    return render(request,'base/test.html',context)


def test_update(request):
    content = Test()
    form = TestForm(instance=content)

    if request.method == 'POST':
        form = TestForm(request.POST,instance=content)
        return redirect('test')
    
    context = {'form':form}
    return render(request,'base/test_update.html',context)\

def createTopic(request):
    if request.method == 'POST':
        tp = TopicForm(request.POST)
        tp.save()
        return redirect('home')
    tp = TopicForm()
    context = {'form':tp}
    return render(request,'base/topic_form.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_dj(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect')

    form = Loginform()
    context = {'form':form}
    return render(request,'base/user_login.html', context)