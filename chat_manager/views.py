from django.shortcuts import render


def index(request):
    return render(request, 'chat_manager/index.html')


def room(request, room_name):
    return render(request, 'chat_manager/room.html', {
        'room_name': room_name
    })
