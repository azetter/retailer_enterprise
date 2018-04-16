from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('안녕하세요 한아름 마트십니다')