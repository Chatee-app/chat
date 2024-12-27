from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
import json
from django.shortcuts import render
@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        # Receive a new message
        data = json.loads(request.body)
        name = data.get("name", "Anonymous")
        content = data.get("content", "")

        if content.strip():
            Message.objects.create(name=name, content=content)

        return JsonResponse({"status": "Message received!"})

    elif request.method == "GET":
        # Retrieve all messages
        messages = Message.objects.order_by("timestamp")
        message_list = [
            {"name": msg.name, "content": msg.content, "timestamp": msg.timestamp.strftime("%Y-%m-%d %H:%M:%S")}
            for msg in messages
        ]
        return JsonResponse({"messages": message_list})




def index(request):
    return render(request, 'chat/index.html')


def ter(request):
    return render(request,'chat/term.html')