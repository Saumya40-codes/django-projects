from django.shortcuts import render, redirect
from .models import Room,Message,Topic
from .forms import RoomForm,LoginForm, SignUpForm
# Create your views here.
def home(request):
    room = Room.objects.all()
    mess = Message.objects.all()
    topic = Topic.objects.all()
    context = {'rooms': room, 'messages': mess, 'topics': topic}
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
            print(request.POST)
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

def userLogin(request):
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if(form.is_valid()):
            form.save()
            print(form.cleaned_data)
            return redirect('home')
    form = LoginForm()
    context = {'form': form}
    return render(request, 'base/user_login.html', context)


def delete(request, pk):
    room= Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})