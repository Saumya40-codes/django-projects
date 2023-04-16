from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def index(request,pk):
    room = rooms[int(pk)-1]
    return render(request, 'base/room.html',{'room_name': room})

def nav(request):
    det = {'info': direc}
    return render(request, 'base/navbar.html', det)


username = input("Enter your name: ")    
passwo = input("Enter your password: ")

direc =[
    {'name':username, 'password':passwo},
]

rooms = [
    {'id': 1, 'name': 'index'},
    {'id': 2, 'name': 'room2'},
    {'id': 3, 'name': 'room3'},
    {'id': 4, 'name': 'room4'},
]