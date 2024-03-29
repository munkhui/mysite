from django.shortcuts import render
import json
from django.http import JsonResponse
from mysite.mqtt import client as mqtt_client
# Create your views here.

def index(request):
  return render(request, 'main/index.html')

def command_center(request):
  return render(request, 'main/command_center.html')


def command_submit(request):
  if request.method == "POST":
    cmd = request.POST.get("your_text")
    mqtt_client.publish('9fmrvy5679/', cmd)
  return render(request, "main/command_center.html")

