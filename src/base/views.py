from django.shortcuts import render, redirect
from .models import Room,Message,Topic, Test, SignUp, Loginpage
from .forms import RoomForm, SignUpForm, TestForm,TopicForm, Loginform
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout , login as login_dj
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    # if(request.user.is_authenticated):
    #     return redirect('home')

    room = Room.objects.filter(
        Q(topic__name__icontains= q) | #only 'contains' is case sensitive matching
        Q(name__icontains= q) |
        Q(description__icontains= q)
        )   

    available_rooms = room.count()    
    context = {'rooms': room, 'top':set(Topic.objects.all()), 'available_rooms': available_rooms}
    return render(request, 'base/home.html', context)
 

def index(request,pk):
    if(request.method == 'POST'):
        room = Room.objects.get(id=pk)
        comments = room.message_set.all().order_by('-cerated')
        message = Message.objects.create(
            user = request.user,
            body = request.POST.get('body'),
            room = room
        )
    context = { 'comment': comments, 'room_name': room}
    return render(request, 'base/room.html',context)

def nav(request):
    det = {'info': direc}
    return render(request, 'base/navbar.html', det)

direc =[
    {'name':'saumya', 'password':'lol'},
]

@login_required(login_url='login')
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
    page = 'signup'
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
                user =  form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login_dj(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Username already taken')
            return redirect('signUp')
    form = UserCreationForm()
    context = {'form': form, 'page': page}
    return render(request, 'base/user_login.html', context)


@login_required(login_url='login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed to do this')

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
        check = Topic.objects.filter(name=tp.data['name'])
        if not check:
            tp.save()
            return redirect('home')
        else:
            messages.error(request,'Topic already exists')
            return redirect('topic_new')
    tp = TopicForm()
    context = {'form':tp}
    return render(request,'base/topic_form.html',context)

def login(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

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
    context = {'form':form, 'page':page}
    return render(request,'base/user_login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def mainSerch(request):
    if request.method == 'POST':
        name = request.POST.get('q')
        room = Room.objects.filter(
            Q(topic__name__icontains= name) | 
            Q(name__icontains= name) |
            Q(description__icontains= name)
        )
        cnt = room.count()
        context = {'rooms': room, 'cnt':cnt}
        return render(request,'base/main_search.html',context)
    return render(request,'base/main_search.html')

def join(request):
    return render(request,'base/join.html')