from django.shortcuts import render, redirect
from .models import Room,Message,Topic, Test
from .forms import RoomForm,LoginForm, SignUpForm, TestForm,TopicForm
from django.db.models import Q
# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    room = Room.objects.filter(
        Q(topic__name__icontains= q) | #only 'contains' is case sensitive matching
        Q(name__icontains= q) |
        Q(description__icontains= q)
        )   

    topic = Topic.objects.all()
    context = {'rooms': room, 'topics': topic, 'top':Topic.objects.all()}
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