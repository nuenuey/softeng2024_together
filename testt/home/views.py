from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse

def reserve(request):
    return render(request, 'home/reserve.html')

def reserve_process(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        # 예약 처리를 수행하고, 성공 메시지 또는 에러 메시지를 반환
        return HttpResponse(f'예약 완료! 이름: {name}, 날짜: {date}')
    return HttpResponse('잘못된 요청입니다.')
# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
