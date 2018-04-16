from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('안녕하세요 하마즈입니다')